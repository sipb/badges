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