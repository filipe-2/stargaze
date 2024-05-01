const header = document.querySelector('#js-header');
let lastScrollTop = 0;

// Função para esconder a barra de navegação ao rolar a tela
function toggleHeaderVisibilityOnScroll() {
    const currentScrollTop = window.scrollY || document.documentElement.scrollTop;

    if (currentScrollTop > lastScrollTop && currentScrollTop > 0) {
        header.classList.add('expanded');
    } else header.classList.remove('expanded');

    lastScrollTop = currentScrollTop;
}

export {
    // Variáveis

    // Funções
    toggleHeaderVisibilityOnScroll,
};