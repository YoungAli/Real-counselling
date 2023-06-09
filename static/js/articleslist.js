const searchBar = document.querySelector('#searchbar');
const searchInput = document.querySelector('#search_input');
const searchBtn = document.querySelector('#search_btn');
const reader = document.querySelector('#article_reader');
const mobileReader = document.querySelector('#mobile_reader');
const gridWrapper = document.querySelector('#article_grid_wrapper');
const articleGrid = document.querySelector('#article_grid');
const mainWrapper = document.querySelector('#articles_main');
const expandGrid = document.querySelector('#expand_grid');
const articleCards = document.getElementsByClassName('card-article');
let tagElements = document.getElementsByClassName('article_tags');

function consolePop(text, dur) {
    let popDiv = document.createElement('div');
    popDiv.id="console_msg_div"
    popDiv.innerHTML = `<div id="console_msg">${text}</div>`;
    document.body.prepend(popDiv);
    let popDivMsg = document.getElementById('console_msg');
    popDivMsg.style.animation = "pop-up 0.3s";
    if(dur =! "infinite"){
        setTimeout(()=>{
            popDivMsg.style.animation = "pop-down 0.3s";
            setTimeout(()=>{document.getElementById('console_msg_div').style.display = 'none'}, 250)
        }, 2000)
    }
};

if (!articleCards.length) {
    console.log(articleCards.length);
    consolePop(`<a href="http://127.0.0.1:8000/articles">No search result, click to refresh articles</a>`, 'infinite')
}

for(let i=0; i< tagElements.length; i++){
    if(tagElements[i].textContent){
        tagElements[i].innerHTML = tagElements[i].textContent.split(',').map(tag => {
            return `<p>${tag}</p>`
        }).slice(0, 4).join(" ");
    }
}

function openReader(){
    mainWrapper.style.animation = "flicker 1s";
    setTimeout(() => {mainWrapper.style.animation = "none"}, 1000);

    if (window.innerWidth >= 800) {
        setTimeout(() => {
            gridWrapper.classList.add('show_reader');
            reader.style.display = "unset";
            expandGrid.style.display = 'unset';
        }, 500);

    } else{
        setTimeout(() => {
            mobileReader.style.display = "block";
            articleGrid.style.display = "none";
        }, 500);
    }
    
}

function closeReader(){
    mainWrapper.style.animation = "flicker 1s"
    setTimeout(() => {mainWrapper.style.animation = "none"}, 1000);
    if (window.innerWidth >= 800){
        setTimeout(() => {
            gridWrapper.classList.remove('show_reader');
            reader.style.display = "none";
            expandGrid.style.display = 'none';
        }, 500);
    } else{
        setTimeout(() => {
            mobileReader.style.display = "none";
            articleGrid.style.display = "unset";
        }, 500);
    }
    
}

function showArticle(title, tags, content, img){
    openReader();
    if (window.innerWidth >= 800){
        setTimeout(() => {
            reader.innerHTML = `<h3 id="reader_title">${title}</h3> ${img? (`<img src="${img}" alt="${title}">`) : ""}
            <div class="article_tags">
            ${tags.split(',').map(tag =>`<p>${tag}</p>`).join(" ")}
            </div>
            <p id="reader_content">${content}</p>`;
        }, 500);
    } else{
        setTimeout(() => {
            mobileReader.innerHTML = `<h3 id="mobile_title">${title}</h3> ${img? (`<img id="mobile_img" src="${img}" alt="${title}">`) : ""}
            <div class="article_tags">
            ${tags.split(',').map(tag =>`<p>${tag}</p>`).join(" ")}
            </div>
            <p id="reader_content">${content}</p>`;
        }, 500);
    }
}

searchInput.addEventListener('keypress', (e)=>{
    if (e.keyCode == 13){
        searchBar.addEventListener('submit', (e)=>{e.preventDefault()})
        searchBtn.click();
    }
})
searchBtn.addEventListener('click', ()=>{
    if (!searchInput.value) {
        consolePop("Error: no search query");
    }
    else{
        closeReader()
        searchBar.submit()
    }
})

expandGrid.addEventListener('click', ()=>{
    closeReader();
})