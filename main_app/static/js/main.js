const nav = document.querySelector('.nav_links');
const mobi_nav = document.querySelector('.mobi_nav_links');

document.querySelector('.cactus_mobi').addEventListener('click', mobi_nav_toggle);
document.querySelector('.cactus').addEventListener('click', nav_toggle);

function mobi_nav_toggle() {
    if (mobi_nav.style.display === "block") {
        mobi_nav.style.display = "none";
    }
    else {
        mobi_nav.style.display = "block";
    }
}

function nav_toggle() {

    if (nav.style.display === "block") {
        nav.style.display = "none";
    }
    else {
        nav.style.display = "block";
    }
}
