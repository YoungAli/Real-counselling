let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let sectionArea = document.querySelector(".home-section");

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
