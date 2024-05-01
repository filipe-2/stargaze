import {
    // Variáveis

    // Funções
    toggleHeaderVisibilityOnScroll,
} from './modules/utils.js';

import {
    // Variáveis
    closeModalBtn,

    // Funções
    closeModal,
} from './modules/missions.js';

// Esconde/expande o header sempre que ocorre rolagem da janela
window.addEventListener('scroll', toggleHeaderVisibilityOnScroll);

// Fecha o modal de missões sempre que o botão de fechá-lo é clicado
closeModalBtn.addEventListener('click', closeModal);