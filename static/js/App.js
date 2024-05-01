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

window.addEventListener('scroll', toggleHeaderVisibilityOnScroll);
closeModalBtn.addEventListener('click', closeModal);