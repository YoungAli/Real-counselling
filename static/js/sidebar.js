let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let sectionArea = document.querySelector(".home-section");
let appointMenu = document.querySelector("#dropdown_btn");
let appointMenuItems = document.getElementsByClassName("appt_menu_items")

function menuBtnChange() {
    if (sidebar.classList.contains("open")) {
        closeBtn.classList.replace("bx-menu", "bx-x")
    } else {
        closeBtn.classList.replace("bx-x", "bx-menu")
    }
}

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();
});

sectionArea && sectionArea.addEventListener("click", () => {
    sidebar.classList.remove("open");
    menuBtnChange();
});

appointMenu.addEventListener('click', ()=>{
    for (let i = 0; i < appointMenuItems.length; i++) {
        appointMenuItems[i].classList.toggle("show_menu_items");
        appointMenu.classList.toggle("dropdown_margin");
    }
})