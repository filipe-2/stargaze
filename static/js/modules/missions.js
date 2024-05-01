const closeModalBtn = document.querySelector('.missions__modal-close');
const missionsModal = document.querySelector('.missions__modal-wrapper');

const closeModal = () => missionsModal.classList.add('modal-closed');

export {
    // Variáveis
    closeModalBtn,
    missionsModal,

    // Funções
    closeModal,
};