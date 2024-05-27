const closeModalBtn = document.querySelector('.missions__modal-close');
const missionsModal = document.querySelector('.missions__modal-wrapper');
const missionsCards = document.querySelectorAll('.missions__card');

// Função para abrir/fechar o modal de missões
const toggleModal = () => missionsModal.classList.toggle('modal-closed');


// ------------------- Exports --------------------
export {
    // Variáveis
    closeModalBtn,
    missionsModal,
    missionsCards,

    // Funções
    toggleModal,
};
// ------------------------------------------------