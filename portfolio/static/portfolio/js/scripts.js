document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("responsive-menu").onclick = function () {
        document.getElementById("myNav").style.width = "100%";
        console.log('a')
    }

    document.querySelector(".closebtn").onclick = function () {
        document.getElementById("myNav").style.width = "0%";
    }

    document.querySelector(".hover-underline").onclick = function () {
        document.getElementById("myNav").style.width = "0%";
    }

    document.querySelector(".hover-underline2").onclick = function () {
        document.getElementById("myNav").style.width = "0%";
    }

    document.querySelector(".hover-underline3").onclick = function () {
        document.getElementById("myNav").style.width = "0%";
    }

    document.querySelector(".hover-underline4").onclick = function () {
        document.getElementById("myNav").style.width = "0%";
    }


    document.querySelector(".button-darkmode").onclick = function () {
        var botao = document.querySelector(".button-darkmode");
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

        const first_content = document.querySelector(".first-content");
        first_content.classList.toggle("dark-mode-first-content");

        const sobremim = document.querySelector(".mainSecond-content");
        sobremim.classList.toggle("dark-mode-second-content");

        const terceira_content = document.querySelector(".terceira-content");
        terceira_content.classList.toggle("dark-mode-terceira-content");

        const grid_content = document.querySelector(".grid-content");
        grid_content.classList.toggle("dark-mode-grid-content");

        const skills = document.querySelector(".mainSkill-content");
        skills.classList.toggle("dark-mode-skill-content");

        const footer = document.querySelector(".footer");
        footer.classList.toggle("dark-mode-footer");

        const map = document.querySelector(".map");
        map.classList.toggle("map-dark-mode");

    };
})









