const nav = document.querySelector('.nav_links');
const mobi_nav = document.querySelector('.mobi_nav_links');
const modal_tog = document.querySelector('.moda_but');
const up_mod = document.querySelector('.vis_blo');
const moda_but = document.querySelector('.moda_but');

document.querySelector('.cactus_mobi').addEventListener('click', mobi_nav_toggle);
document.querySelector('.cactus').addEventListener('click', nav_toggle);
document.querySelector('.moda_but').addEventListener('click', display_mod);
document.querySelector('.close_moda').addEventListener('click', display_mod);

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

function display_mod() {
    if (up_mod.style.visibility === "hidden") {
        up_mod.visibility = "inherit";
        moda_but.classList.add("is-loading")
        up_mod.style.display = "block";
    }
    else {
        moda_but.classList.remove("is-loading")
        up_mod.style.visibility = "hidden";
        up_mod.style.display = "none";
    }
}