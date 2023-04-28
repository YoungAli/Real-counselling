const menuBtn = document.querySelector('#menu-button');
const mobileMenu = document.querySelector('#mobile-nav');
const menuBack = document.querySelector("#back-button");
const mobileNavLink = document.querySelectorAll('.mobile-nav-links');
const mobileNavBlind = document.querySelector('#mobile-nav-blind');

menuBtn.addEventListener('click', () =>{
mobileMenu.style.display = 'flex';

mobileMenu.style.animation ='slide-left 0.7s';

mobileNavBlind.style.display ="unset"

})

const menuClose = () =>{
mobileMenu.style.animation ='slide-right 0.7s';

mobileNavBlind.style.display ="none"
setTimeout(()=>{
    mobileMenu.style.display = 'none'

}, 650)
}


mobileNavBlind.addEventListener('click', menuClose);

mobileNavLink.forEach(link => {
    link.addEventListener('click', menuClose)
});
menuBack.addEventListener('click', menuClose);