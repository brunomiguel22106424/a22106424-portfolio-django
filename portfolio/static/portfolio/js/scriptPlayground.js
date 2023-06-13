document.addEventListener('DOMContentLoaded', function() {
    const display = document.querySelector(".display");
    const buttons = document.querySelectorAll("button");


    buttons.forEach((btn) => {
        btn.addEventListener("click", () => {
            if (btn.id === "=") {
                display.value = eval(display.value);
            } else if (btn.id === "ac") {
                display.value = "";
            } else if (btn.id === "de") {
                display.value = display.value.slice(0, -1);
            } else {
                display.value += btn.id;
            }
        });
    });
})

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector(".button-darkmode2").onclick = function () {
        var botao = document.querySelector(".button-darkmode2");
        var bola = document.querySelector(".ball");

        if (window.innerWidth > "600") {
            if (botao.style.backgroundColor === "whitesmoke") {
                botao.style.backgroundColor = "#1a1919";
                bola.style.backgroundColor = "whitesmoke";
                bola.style.transform = "translateX(0px)";
            } else {
                botao.style.backgroundColor = "whitesmoke";
                bola.style.backgroundColor = "#1a1919";
                bola.style.transform = "translateX(2vw)";
            }
        } else {
            if (botao.style.backgroundColor === "whitesmoke") {
                botao.style.backgroundColor = "#1a1919";
                bola.style.backgroundColor = "whitesmoke";
                bola.style.transform = "translateX(0px)";
            } else {
                botao.style.backgroundColor = "whitesmoke";
                bola.style.backgroundColor = "#1a1919";
                bola.style.transform = "translateX(4vw)";
            }
        }

        const header = document.querySelector(".header");
        header.classList.toggle("dark-mode-header");

        const first_content_c = document.querySelector(".first-content-c");
        first_content_c.classList.toggle("dark-mode-first-content-c");

        const second_content_c = document.querySelector(".second-content-c");
        second_content_c.classList.toggle("dark-mode-second-content-c");

    };
})

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('form').onsubmit = function () {
        const opiniao = document.querySelector('#opiniao_user').value;
        document.querySelector('p').innerHTML = `Opinião: ${opiniao}`;

        const nome = document.querySelector('#nome').value;
        document.querySelector('.nome1 p').innerHTML = `${nome}`;
        document.querySelector('.nome2 p').innerHTML = `${nome}`;
        document.querySelector('.nome3 p').innerHTML = `${nome}`;
        return false;
    };
});

document.addEventListener('DOMContentLoaded', function() {
    const mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Augosto", "Setembro", "Outubro", "Novembro", "Decemmbro"];

    const d = new Date();
    let day = d.getDate();
    let month = mes[d.getMonth()];
    let year = d.getFullYear();
    document.querySelector('.datatoday p').innerHTML = `${day} de ${month}, ${year}`;

})

document.addEventListener('DOMContentLoaded', function() {
    const input1 = document.getElementById('opiniao_user');
    input1.addEventListener('mouseover', function handleMouseOver() {
        input1.style.backgroundColor = '#eabe68';
    });

    input1.addEventListener('mouseout', function handleMouseOver() {
        input1.style.backgroundColor = 'rgba(255, 255, 255, 0.19)';
    });

    const input2 = document.getElementById('nome');
    input2.addEventListener('mouseover', function handleMouseOver() {
        input2.style.backgroundColor = '#eabe68';
    });

    input2.addEventListener('mouseout', function handleMouseOver() {
        input2.style.backgroundColor = 'rgba(255, 255, 255, 0.19)';
    });

    const sub = document.getElementById('submit');
    sub.addEventListener('mouseover', function handleMouseOver() {
        sub.style.backgroundColor = 'rgba(0, 0, 0, 0.30)';
    });

    sub.addEventListener('mouseout', function handleMouseOver() {
        sub.style.backgroundColor = 'rgba(0, 0, 0, 0.19)';
    });

})

