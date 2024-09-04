document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", function (event) {
        const username = form.username.value.trim();
        const password = form.password.value.trim();

        if (username === "" || password === "") {
            alert("Por favor, preencha todos os campos.");
            event.preventDefault(); // Impede o envio do formulário
            return;
        }

        if (password.length < 6) {
            alert("A senha deve ter pelo menos 6 caracteres.");
            event.preventDefault();
            return;
        }

        // Adicione outras validações se necessário

        // Se todas as validações passarem, o formulário será enviado
    });
});
