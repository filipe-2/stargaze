import {
    // Variáveis

    // Funções
    toggleHeaderVisibilityOnScroll,
} from './modules/utils.js';

window.addEventListener('scroll', toggleHeaderVisibilityOnScroll);

const closeModalBtn = document.querySelector('.missions__modal-close');
const missionsModal = document.querySelector('.missions__modal-wrapper');

closeModalBtn.addEventListener('click', () => missionsModal.classList.add('modal-closed'));

console.log(closeModalBtn);