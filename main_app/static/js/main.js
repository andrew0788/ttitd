const nav = document.querySelector('.nav_links');
const mobi_nav = document.querySelector('.mobi_nav_links');
const modal_tog = document.querySelector('.moda_but');
const up_mod = document.querySelector('.vis_blo');
const moda_but = document.querySelector('.moda_but');
const navBar = document.querySelector('.navbar-menu')
const y_vid = document.querySelector('.back-vid');
const subtitleOpen = document.querySelector('.subtitle-container');
const skyHigh = document.getElementById('sky-high');
const startIt = document.getElementById('startup');
const subtitleSky = document.getElementById('subtitle-sky');
const clubKid = document.getElementById('club-kid');
const subtitleClub = document.getElementById('subtitle-club');
const artTrip = document.getElementById('art-trip');
const subtitleArt = document.getElementById('subtitle-art');
const subtitleEnd = document.getElementById('subtitle-end');
const openArea = document.querySelector('.disp-none');
const stickySignup = document.querySelector('div.sticky-form');
const openerTitles = document.getElementById('titleCactus');
var openTimeVid

document.querySelector('.cactus').addEventListener('click', nav_toggle);
document.querySelector('.cactus_mobi').addEventListener('click', mobi_nav_toggle);
document.querySelector('.sticky-signup').addEventListener('click', showSignForm);
document.getElementById('startup').addEventListener('mouseenter', showVid, false);

function showSignForm() {
            if (stickySignup.style.display === "block") {
                stickySignup.style.display = "none";
                openerTitles.style.display = "none";
            }
            else {
                stickySignup.style.display = "block";
                
            }
        };

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

function showVid() {
    navBar.style.display = "none";
    skyHigh.style.display = "block";
    startIt.style.visibility = "hidden";
    subtitleOpen.style.display = "none";
    openTimeVid = setTimeout(showSkySub, 3000);
}

function showSkySub() {
    subtitleSky.style.display = "block"
    openTimeVid = setTimeout(showClub, 5000);
}

function showClub() {
    subtitleSky.style.display = "none"
    skyHigh.style.display = "none"
    clubKid.style.display = "block"
    subtitleClub.style.display = "block"
    openTimeVid = setTimeout(showArt, 4000);
}

function showArt() {
    clubKid.style.display = "none"
    subtitleClub.style.display = "none"
    artTrip.style.display = "block"
    subtitleArt.style.display = "block"
    openTimeVid = setTimeout(showEnd, 4000);
}

function showEnd() {
    subtitleArt.style.display = "none"
    subtitleEnd.style.display = "block"
    openTimeVid = setTimeout(showAll, 3000);
}

function showAll() {
    navBar.style.display = "block";
    artTrip.style.display = "none";
    subtitleEnd.style.display = "none";
    openArea.style.display = "block";
}



// lazy load
document.addEventListener("DOMContentLoaded", function () {
    var lazyImages = [].slice.call(document.querySelectorAll("img.lazy"));;

    if ("IntersectionObserver" in window && "IntersectionObserverEntry" in window && 
    "intersectionRatio" in window.IntersectionObserverEntry.prototype) {
        let lazyImageObserver = new IntersectionObserver(function (entries, observer) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    let lazyImage = entry.target;
                    lazyImage.src = lazyImage.dataset.src;
                    lazyImage.srcset = lazyImage.dataset.srcset;
                    lazyImage.classList.remove("lazy");
                    lazyImageObserver.unobserve(lazyImage);
                }
            });
        });

        lazyImages.forEach(function (lazyImage) {
            lazyImageObserver.observe(lazyImage);
        });
    }
})