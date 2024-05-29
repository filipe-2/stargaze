// ------------------- Imports --------------------
// Módulo utils
import {
    // Variáveis
    hideHeaderBtn,

    // Funções
    toggleHeaderVisibilityOnScroll,
    toggleHeaderVisibilityOnClick,
} from './modules/utils.js';


// Módulo missions
import {
    // Variáveis
    closeModalBtn,
    missionsCards,
    missionsModal,
    form,
    closeFormBtn,
    addCardBtn,

    // Funções
    toggleModal,
} from './modules/missions.js';
// ------------------------------------------------


// Esconde/expande o header sempre que ocorre rolagem da janela
window.addEventListener('scroll', toggleHeaderVisibilityOnScroll);

// Fecha o modal de missões sempre que o botão de fechá-lo é clicado
closeModalBtn.addEventListener('click', () => toggleModal(missionsModal));

closeFormBtn.addEventListener('click', () => toggleModal(form));
hideHeaderBtn.addEventListener('click', toggleHeaderVisibilityOnClick);
missionsCards.forEach((card) => card.addEventListener('click', () => toggleModal(missionsModal)));
addCardBtn.addEventListener('click', () => toggleModal(form));

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.missions__submit').addEventListener('click', (event) => {
        event.preventDefault();

        var name = document.getElementById('name').value;
        var dateLaunch = document.getElementById('date-launch').value;
        var dateReturn = document.getElementById('date-return').value;
        var destiny = document.getElementById('destiny').value;
        var status = document.getElementById('status').value;
        var crew = document.getElementById('crew').value;
        var load = document.getElementById('load').value;
        var cost = document.getElementById('cost').value;
        var statusDetails = document.getElementById('status-details').value;

        var data = {
            name: name,
            date_launch: dateLaunch,
            date_return: dateReturn,
            destiny: destiny,
            status: status,
            crew: crew,
            load: load,
            cost: cost,
            status_details: statusDetails,
        };

        fetch('/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then((res) => {
            if (!res.ok) throw new Error('Erro ao adicionar missão');

            console.log('Missão adicionada com sucesso!');
            toggleModal(form);
        })
        .catch((err) => {
            console.error('Erro ao adicionar missão: ', err.message);
        })
    })
});