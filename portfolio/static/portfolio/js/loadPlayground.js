var i = setInterval(function () {
    clearInterval(i);

    document.getElementById("loading").style.display = "none";
    document.querySelector(".first-content-c").style.display = "flex";
    document.querySelector(".header").style.display = "flex";
    document.querySelector(".second-content-c").style.display = "flex";

}, 2000);