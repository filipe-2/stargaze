const closeModalBtn = document.querySelector('.missions__modal-close');
const missionsModal = document.querySelector('.missions__modal-wrapper');

// Função para fechar o modal de missões
const closeModal = () => missionsModal.classList.add('modal-closed');


// ------------------- Exports --------------------
export {
    // Variáveis
    closeModalBtn,
    missionsModal,

    // Funções
    closeModal,
};
// ------------------------------------------------