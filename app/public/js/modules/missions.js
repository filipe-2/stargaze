const closeModalBtn = document.querySelector('.missions__modal-close');
const missionsModal = document.querySelector('.missions__modal-wrapper');
const missionsCards = document.querySelectorAll('.missions__card');
const form = document.querySelector('.missions__modal-form');
const addCardBtn = document.querySelector('.missions__add-card');

// Função para abrir/fechar o modal de missões
const toggleModal = (modal) => modal.classList.toggle('modal-closed');


// ------------------- Exports --------------------
export {
    // Variáveis
    closeModalBtn,
    missionsModal,
    missionsCards,
    form,
    addCardBtn,

    // Funções
    toggleModal,
};
// ------------------------------------------------