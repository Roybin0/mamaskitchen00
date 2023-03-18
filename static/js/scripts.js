var medium_screen = window.matchMedia("(max-width: 768px)")
var small_screen = window.matchMedia("(max-width: 576px)")

function changeFooter(screen_size) {
    if (screen_size.matches) { 
        footer = document.getElementById("footer"); 
        footer.classList.remove("fixed-bottom");
    } 
}
