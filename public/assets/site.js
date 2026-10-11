// Progressive explanation tabs. The initial HTML contains every panel for all readers.
const tablist = document.querySelector('.steps');
if (tablist) {
  const tabs = [...tablist.querySelectorAll('a')];
  const panels = tabs.map(tab => document.querySelector(tab.getAttribute('href')));
  tablist.setAttribute('role', 'tablist');
  tabs.forEach((tab, index) => {
    tab.setAttribute('role', 'tab');
    tab.setAttribute('aria-controls', panels[index].id);
    panels[index].setAttribute('role', 'tabpanel');
    panels[index].tabIndex = 0;
  });
  const select = (index, focus = false) => {
    tabs.forEach((tab, position) => {
      const active = position === index;
      tab.setAttribute('aria-selected', String(active));
      tab.tabIndex = active ? 0 : -1;
      panels[position].hidden = !active;
    });
    if (focus) tabs[index].focus();
  };
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', event => {
      event.preventDefault();
      select(index);
    });
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) {
        event.preventDefault();
        select(next, true);
      }
    });
  });
  const initial = panels.findIndex(panel => `#${panel.id}` === location.hash);
  select(initial < 0 ? 0 : initial);
  window.addEventListener('hashchange', () => {
    const index = panels.findIndex(panel => `#${panel.id}` === location.hash);
    if (index >= 0) select(index);
  });
}
