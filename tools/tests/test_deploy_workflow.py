"""Exercise the actual deployment verification shell's bounded retry behavior."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[2]


class DeploymentVerificationTests(unittest.TestCase):
    def verify_attempts(self, failures):
        workflow = (ROOT / ".github/workflows/deploy-swa-eylema-dev.yml").read_text()
        step = workflow.split("      - name: Verify live canonical host\n", 1)[1]
        script = textwrap.dedent(step.split("        run: |\n", 1)[1])
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            calls = folder / "calls"
            verifier = folder / "python"
            verifier.write_text(f"#!{sys.executable}\n" + textwrap.dedent("""\
                import os
                from pathlib import Path
                import sys
                expected = ['tools/check_live.py', '--url', os.environ['SITE_URL'], '--commit', os.environ['GITHUB_SHA']]
                if sys.argv[1:] != expected:
                    sys.exit(9)
                record = Path(os.environ['CHECK_CALLS'])
                count = int(record.read_text()) + 1 if record.exists() else 1
                record.write_text(str(count))
                sys.exit(1 if count <= int(os.environ['FAILURES']) else 0)
                """))
            verifier.chmod(0o755)
            sleeper = folder / "sleep"
            sleeper.write_text(f"#!{sys.executable}\n")
            sleeper.chmod(0o755)
            env = dict(os.environ, PATH=str(folder) + os.pathsep + os.environ["PATH"],
                       SITE_URL="https://eyleme.dev", GITHUB_SHA="a" * 40,
                       CHECK_CALLS=str(calls), FAILURES=str(failures))
            result = subprocess.run(["bash", "-e", "-c", script], env=env,
                                    capture_output=True, text=True, timeout=10)
            return result.returncode, int(calls.read_text())

    def test_current_release_passes_without_extra_attempts(self):
        self.assertEqual(self.verify_attempts(0), (0, 1))

    def test_propagating_release_must_eventually_pass_the_same_check(self):
        self.assertEqual(self.verify_attempts(2), (0, 3))

    def test_persistent_mismatch_fails_after_three_attempts(self):
        self.assertEqual(self.verify_attempts(20), (1, 3))
