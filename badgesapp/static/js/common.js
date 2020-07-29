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

var accordionList = document.getElementsByClassName("accordion-button");
for (const acc of accordionList) {
    acc.addEventListener("click", function () {
        var parent = this.parentNode;
        parent.classList.toggle("active");
        var panelList = parent.getElementsByClassName("panel");
        for (const panel of panelList) {
            if (panel.style.display === "flex") {
                panel.style.display = "none";
            } else {
                panel.style.display = "flex";
            }
        }
    });
}