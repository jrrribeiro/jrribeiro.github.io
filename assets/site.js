function applyLanguage(language) {
  const selected = language === 'en' ? 'en' : 'pt';
  document.documentElement.lang = selected === 'pt' ? 'pt-BR' : 'en';
  localStorage.setItem('jrribeiro-language', selected);

  document.querySelectorAll('[data-lang]').forEach((node) => {
    const active = node.getAttribute('data-lang') === selected;
    node.classList.toggle('is-active', active);
  });

  document.querySelectorAll('[data-lang-toggle]').forEach((button) => {
    const active = button.getAttribute('data-lang-toggle') === selected;
    button.classList.toggle('is-active', active);
    button.setAttribute('aria-pressed', String(active));
  });
}

function initializeLanguageToggle() {
  const savedLanguage = localStorage.getItem('jrribeiro-language');
  applyLanguage(savedLanguage || 'pt');

  document.querySelectorAll('[data-lang-toggle]').forEach((button) => {
    button.addEventListener('click', () => applyLanguage(button.getAttribute('data-lang-toggle')));
  });
}

function initializeActiveNav() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav a').forEach((link) => {
    const target = link.getAttribute('href').split('/').pop();
    if (target === currentPath) {
      link.classList.add('is-active');
      link.setAttribute('aria-current', 'page');
    }
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initializeLanguageToggle();
  initializeActiveNav();
});
