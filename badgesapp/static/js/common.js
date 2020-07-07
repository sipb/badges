function hamburger() {
    var links = document.getElementById("navlinks");
    if (links.style.display == "block") {
        links.style.display = "none";
    } else {
        links.style.display = "block";
    }
}

function headerSearch() {
    var search = document.getElementById("header-search");
    if (search.style.display == "flex") {
        search.style.display = "none";
    } else {
        search.style.display = "flex";
    }
}

var accordionList = document.getElementsByClassName("accordion");
for (const acc of accordionList) {
    acc.addEventListener("click", function () {
        this.classList.toggle("active");
        var panelList = acc.getElementsByClassName("panel");
        for (const panel of panelList) {
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        }
    });
}