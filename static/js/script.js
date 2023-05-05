//base scripts

const menuBtn = document.querySelector('#menu-button');
const mobileMenu = document.querySelector('#mobile-nav');
const menuBack = document.querySelector("#back-button");
const mobileNavLink = document.querySelectorAll('.mobile-nav-links');
const mobileNavBlind = document.querySelector('#mobile-nav-blind');
const navBar = document.querySelector('#main-nav');

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

window.addEventListener('scroll', ()=>{
    if(this.scrollY >= 40){
        navBar.classList.add('main-nav-bg');
    }
    else{
        navBar.classList.remove('main-nav-bg');  
    }
})

