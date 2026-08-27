(() => {
  'use strict';

  const root = document.documentElement;
  root.classList.add('js-enabled');

  const header = document.querySelector('[data-site-header]');
  const toggle = document.querySelector('[data-menu-toggle]');
  const navigation = document.querySelector('[data-site-nav]');

  if (header && toggle && navigation) {
    const desktopQuery = window.matchMedia('(min-width: 56rem)');

    const setMenuState = (isOpen, returnFocus = false) => {
      toggle.setAttribute('aria-expanded', String(isOpen));
      header.classList.toggle('is-menu-open', isOpen);
      navigation.classList.toggle('is-open', isOpen);

      if (desktopQuery.matches) {
        navigation.removeAttribute('hidden');
      } else {
        navigation.toggleAttribute('hidden', !isOpen);
      }

      if (returnFocus) {
        toggle.focus();
      }
    };

    toggle.hidden = false;
    setMenuState(false);

    toggle.addEventListener('click', () => {
      const isOpen = toggle.getAttribute('aria-expanded') !== 'true';
      setMenuState(isOpen);
    });

    navigation.addEventListener('click', (event) => {
      if (event.target.closest('a')) {
        setMenuState(false);
      }
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setMenuState(false, true);
      }
    });

    document.addEventListener('click', (event) => {
      if (
        toggle.getAttribute('aria-expanded') === 'true' &&
        !header.contains(event.target)
      ) {
        setMenuState(false);
      }
    });

    const closeAtDesktopWidth = () => setMenuState(false);

    if (typeof desktopQuery.addEventListener === 'function') {
      desktopQuery.addEventListener('change', closeAtDesktopWidth);
    } else {
      desktopQuery.addListener(closeAtDesktopWidth);
    }
  }

  const currentYear = String(new Date().getFullYear());
  document.querySelectorAll('[data-current-year]').forEach((node) => {
    node.textContent = currentYear;
  });
})();
