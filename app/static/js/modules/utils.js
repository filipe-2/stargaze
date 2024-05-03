const header = document.querySelector('#js-header');
const hideHeaderBtn = document.querySelector('.hide-nav');
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


// Função para esconder a barra de navegação ao clicar no botão de esconder
function toggleHeaderVisibilityOnClick() {
    if (header.classList.contains('expanded')) header.classList.remove('expanded');
    else header.classList.add('expanded');

    toggleIconOfHideHeaderBtn();
}


// Função para trocar o ícone do botão de esconder o header
function toggleIconOfHideHeaderBtn() {
    hideHeaderBtn.firstElementChild.classList.toggle('fa-chevron-down');
    hideHeaderBtn.firstElementChild.classList.toggle('fa-chevron-up');
}


// ------------------- Exports --------------------
export {
    // Variáveis
    hideHeaderBtn,

    // Funções
    toggleHeaderVisibilityOnScroll,
    toggleHeaderVisibilityOnClick
};
// ------------------------------------------------