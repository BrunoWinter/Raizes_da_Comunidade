console.log('lendo js');
document.addEventListener("DOMContentLoaded", function() {
    const modalButtons = document.querySelectorAll(".modalButton");
    const modalCloseButtons = document.querySelectorAll(".modalCloseButton");
    const modals = document.querySelectorAll(".modal");

    /*modalButtons.forEach(function(button, index) {
        button.addEventListener("click", function() {
            modals[index].showModal();
        })
    })*/

    modalButtons.array.forEach(function(button, index) {
        console.log('botão clicado');
        button.addEventListener("click", function() {
            modals[index].showModal();
        })
    });

    modalCloseButtons.forEach(function(button, index) {
        button.addEventListener("click", function() {
            modals[index].close();
        });
    });

    modals.forEach(function(modal) {
        modal.addEventListener("click", function(event) {
            if (event.target === modal) {
                modal.close();
            }
        });
    });

})