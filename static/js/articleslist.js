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
let contentArray = document.getElementsByClassName('content_parameter');

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
            if(tag != "" && tag != " ")
            return `<p>${tag}</p>`
        }).slice(0, 2).join(" ");
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
    //Uncomment this in case of unforseen disaster
    // if (window.innerWidth >= 800){
    //     setTimeout(() => {
    //         gridWrapper.classList.remove('show_reader');
    //         reader.style.display = "none";
    //         expandGrid.style.display = 'none';
    //     }, 500);
    // } else{
    //     setTimeout(() => {
    //         mobileReader.style.display = "none";
    //         articleGrid.style.display = "grid";
    //     }, 500);
    // }
    setTimeout(() => {
                gridWrapper.classList.remove('show_reader');
                reader.style.display = "none";
                expandGrid.style.display = 'none';
                mobileReader.style.display = "none";
                articleGrid.style.display = "grid";
            }, 500);
}
function showArticle(title, tags, img){
    let content = "Content Error";
    for (let i = 0; i < contentArray.length; i++) {
        let contentTitle = contentArray[i].textContent.split('&s#3DEMACATION');
        console.log(contentTitle);
        if(contentTitle[1] == title){content = contentTitle[0]}
    }
    openReader();
    if (window.innerWidth >= 800){
        setTimeout(() => {
            reader.innerHTML = `<h3 id="reader_title">${title}</h3> ${img? (`<img src="${img}" alt="${title}">`) : ""}
            <div class="article_tags">
            ${tags.split(',').map(tag =>{
                if(tag != "" && tag != " ")
                return `<p>${tag}</p>`
            }).join(" ")}
            </div>
            <p id="reader_content"></p>`;
            document.querySelector('#reader_content').innerHTML = content.split('\n').join('<br />');
        }, 500);
    } else{
        setTimeout(() => {
            mobileReader.innerHTML = `<div id="close_mobile_btn">&#8592; Back</div><h3 id="mobile_title">${title}</h3> ${img? (`<img id="mobile_img" src="${img}" alt="${title}">`) : ""}
            <div class="article_tags">
            ${tags.split(',').map(tag =>{
                if(tag != "" && tag != " ")
                return `<p>${tag}</p>`
            }).join(" ")}
            </div>
            <p id="mobile_reader_content"></p>`;

            document.querySelector('#mobile_reader_content').innerHTML = content.split('\n').join('<br />');

            document.querySelector('#close_mobile_btn').addEventListener('click', ()=>{
                closeReader();
                console.log('hello');
            })
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
        searchBar.submit()
    }
})

expandGrid.addEventListener('click', ()=>{
    closeReader();
});

