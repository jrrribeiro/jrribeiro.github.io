document.documentElement.classList.add('js-enabled');
const menuButton = document.querySelector('.menu-button');
const navigation = document.querySelector('.main-nav');

function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.setAttribute('aria-label', 'Abrir menu');
  navigation.classList.remove('is-open');
}

menuButton.addEventListener('click', () => {
  const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!isOpen));
  menuButton.setAttribute('aria-label', isOpen ? 'Abrir menu' : 'Fechar menu');
  navigation.classList.toggle('is-open', !isOpen);
});

navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
document.querySelector('#year').textContent = new Date().getFullYear();

const requestMessage = document.querySelector('#request-message');
if (requestMessage) {
  const articleDoi = new URLSearchParams(window.location.search).get('artigo');
  if (articleDoi && /^10\.\d{4,9}\/[\w.();/:+-]+$/i.test(articleDoi)) {
    requestMessage.value = `Olá, Jonathan! Gostaria de solicitar uma cópia do artigo com DOI ${articleDoi}. Obrigado(a)!`;
    document.querySelector('#solicitar-copia').scrollIntoView({ block: 'start' });
  }

  const emailLink = document.querySelector('#request-email');
  const updateEmailLink = () => {
    const subject = articleDoi ? `Solicitação de artigo: ${articleDoi}` : 'Contato pelo ConectAves';
    emailLink.href = `mailto:jonathan2008r@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(requestMessage.value)}`;
  };
  updateEmailLink();
  requestMessage.addEventListener('input', updateEmailLink);
  document.querySelector('#request-copy-button').addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(requestMessage.value);
      document.querySelector('#request-feedback').textContent = 'Mensagem copiada.';
    } catch {
      document.querySelector('#request-feedback').textContent = 'Selecione e copie a mensagem acima.';
      requestMessage.focus();
      requestMessage.select();
    }
  });
}
