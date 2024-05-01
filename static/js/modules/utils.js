const header = document.querySelector('#js-header');
let lastScrollTop = 0;

// Função para esconder a barra de navegação ao rolar a tela
function toggleHeaderVisibilityOnScroll() {
    const currentScrollTop = window.scrollY || document.documentElement.scrollTop;

    // Checa se a posição de rolagem atual é maior que zero e que a última rolagem
    if (currentScrollTop > lastScrollTop && currentScrollTop > 0) {
        // Expande o header
        header.classList.add('expanded');
    } else {
        // Colapsa o header
        header.classList.remove('expanded');
    }

    // Atualiza a última posição da rolagem para a atual
    lastScrollTop = currentScrollTop;
}


// ------------------- Exports --------------------
export {
    // Variáveis

    // Funções
    toggleHeaderVisibilityOnScroll,
};
// ------------------------------------------------