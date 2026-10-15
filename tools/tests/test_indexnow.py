"""IndexNow must preflight the new host and send at most one explicit POST."""
from contextlib import redirect_stdout, redirect_stderr
from email.message import Message
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch, Mock
from urllib.error import HTTPError, URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import indexnow
from build import ROOT


class Response:
    def __init__(self, url, body, mime="text/html", status=200, robots=None):
        self.url, self.body, self.status = url, body, status
        self.headers = Message()
        self.headers['Content-Type'] = mime
        if robots is not None:
            self.headers['X-Robots-Tag'] = robots
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self, count): return self.body[:count]
    def geturl(self): return self.url


class IndexNowTests(unittest.TestCase):
    def responses(self, status=200):
        data = indexnow.payload()
        return [Response(data['keyLocation'], data['key'].encode(), 'text/plain'),
                Response(data['urlList'][0], (ROOT/'public/index.html').read_bytes()),
                Response(data['urlList'][1], (ROOT/'public/tr/index.html').read_bytes()),
                Response(indexnow.ENDPOINT, b'', 'text/plain', status)]

    def run_mocked(self, responses):
        opener = Mock()
        opener.open.side_effect = responses
        with patch('indexnow.build_opener', return_value=opener):
            receipt = indexnow.submit()
        return opener, receipt

    def test_preview_has_zero_network_access(self):
        with patch('indexnow.build_opener') as build, redirect_stdout(io.StringIO()) as output:
            self.assertEqual(indexnow.main([]), 0)
        build.assert_not_called()
        preview=json.loads(output.getvalue())
        self.assertEqual(preview['mode'], 'preview_only')
        self.assertTrue(preview['submissionEnabled'])
        self.assertEqual(preview['payload'], indexnow.payload())

    def test_cli_preview_and_retained_key(self):
        result=subprocess.run([sys.executable, str(ROOT/'tools/indexnow.py')], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout)['mode'], 'preview_only')
        data=indexnow.payload()
        self.assertEqual((ROOT/'public'/f'{data["key"]}.txt').read_bytes(), data['key'].encode())

    def test_rejects_old_foreign_duplicate_urls_and_invalid_key_before_network(self):
        for field, value in [('host','eylema.dev'),('key','bad'),('keyLocation','https://foreign.test/key.txt'),
                             ('urlList',['https://eylema.dev/','https://eyleme.dev/tr/']),
                             ('urlList',['https://eyleme.dev/','https://eyleme.dev/']),
                             ('urlList',['https://eyleme.dev/'])]:
            data=indexnow.payload(); data[field]=value
            with self.subTest(field=field,value=value), patch('indexnow.payload',return_value=data), patch('indexnow.build_opener') as build:
                with self.assertRaises(ValueError): indexnow.submit()
                build.assert_not_called()

    def test_bad_key_body_mime_status_or_redirect_prevents_post(self):
        for change in ('body','mime','status','redirect','blocking_header'):
            responses=self.responses(); key=responses[0]
            if change=='body': key.body=b'wrong-key'
            if change=='mime': key.headers.replace_header('Content-Type','text/html')
            if change=='status': key.status=404
            if change=='redirect': key.url='https://foreign.test/key.txt'
            if change=='blocking_header': key.headers['X-Robots-Tag']='noindex'
            opener=Mock(); opener.open.side_effect=responses
            with self.subTest(change=change), patch('indexnow.build_opener',return_value=opener):
                with self.assertRaises(ValueError): indexnow.submit()
                self.assertEqual(opener.open.call_count,1)

    def test_each_landing_page_must_be_indexable_and_canonical(self):
        for position in (1,2):
            for change in ('noindex','header','canonical','mime','status','redirect','oversized'):
                responses=self.responses(); page=responses[position]
                if change=='noindex': page.body=page.body.replace(b'content="index,follow"',b'content="noindex,follow"')
                if change=='header': page.headers['X-Robots-Tag']='noindex,follow'
                if change=='canonical': page.body=page.body.replace(b'rel="canonical"',b'rel="other"')
                if change=='mime': page.headers.replace_header('Content-Type','text/plain')
                if change=='status': page.status=500
                if change=='redirect': page.url+='unexpected'
                if change=='oversized': page.body=b'x'*(indexnow.LIMIT+1)
                opener=Mock(); opener.open.side_effect=responses
                with self.subTest(position=position,change=change), patch('indexnow.build_opener',return_value=opener):
                    with self.assertRaises(ValueError): indexnow.submit()
                    self.assertEqual(opener.open.call_count,position+1)

    def test_actual_status_and_single_batch_are_preserved_without_retry(self):
        for status in (200,202,403,422,429,500,302):
            opener, receipt=self.run_mocked(self.responses(status))
            with self.subTest(status=status):
                self.assertEqual(opener.open.call_count,4)
                req=opener.open.call_args_list[-1].args[0]
                self.assertEqual(req.get_method(),'POST')
                self.assertEqual(req.full_url,indexnow.ENDPOINT)
                self.assertEqual(json.loads(req.data),indexnow.payload())
                self.assertEqual(receipt['httpStatus'],status)
                self.assertFalse(receipt['indexingConfirmed'])
                self.assertEqual(receipt['outcome'],{200:'submitted',202:'key_validation_pending'}.get(status,'rejected'))

    def test_http_error_body_and_retry_after_are_recorded(self):
        responses=self.responses(); headers=Message(); headers['Retry-After']='120'
        responses[-1]=HTTPError(indexnow.ENDPOINT,429,'Too many requests',headers,io.BytesIO(b'limited'))
        opener, receipt=self.run_mocked(responses)
        self.assertEqual(receipt['httpStatus'],429)
        self.assertEqual(receipt['responseBody'],'limited')
        self.assertEqual(receipt['retryAfter'],'120')
        self.assertEqual(opener.open.call_count,4)

    def test_connection_failure_is_not_retried_or_reported_as_success(self):
        responses=self.responses(); responses[-1]=URLError('offline')
        opener=Mock(); opener.open.side_effect=responses
        with patch('indexnow.build_opener',return_value=opener):
            with self.assertRaises(URLError): indexnow.submit()
        self.assertEqual(opener.open.call_count,4)

    def test_existing_receipt_refuses_before_submission(self):
        with tempfile.TemporaryDirectory() as directory:
            receipt=Path(directory)/'receipt.json'; receipt.write_text('original')
            with patch('indexnow.submit') as submit, redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as stopped:
                    indexnow.main(['--submit','--receipt',str(receipt)])
            self.assertEqual(stopped.exception.code,2)
            submit.assert_not_called()
            self.assertEqual(receipt.read_text(),'original')

    def test_redirect_handler_never_replays_post(self):
        self.assertIsNone(indexnow.NoRedirect().redirect_request(None,None,302,'Found',{},'https://foreign.test'))


if __name__=='__main__': unittest.main()
