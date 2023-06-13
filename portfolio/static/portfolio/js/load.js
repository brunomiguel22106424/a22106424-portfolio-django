document.addEventListener('DOMContentLoaded', function() {
    var i = setInterval(function () {
        clearInterval(i);

        document.getElementById("loading").style.display = "none";
        document.querySelector(".first-content").style.display = "flex";
        document.getElementById("aboutme").style.display = "flex";
        document.querySelector(".header").style.display = "-ms-flex";
        document.querySelector(".grid-content").style.display = "grid";
        document.querySelector(".terceira-content").style.display = "flex";
        document.querySelector(".footer").style.display = "flex";

    }, 2000);
})