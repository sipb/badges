function hamburgerFunc() {
    var links = document.getElementById("navlinks");
    if (links.style.display == "block") {
        links.style.display = "none";
    } else {
        links.style.display = "block";
    }
}