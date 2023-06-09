const searchBar = document.querySelector('#searchbar');
const searchInput = document.querySelector('#search_input');
const searchBtn = document.querySelector('#search_btn');
const reader = document.querySelector('#article_reader');
const GridWrapper = document.querySelector('#article_grid_wrapper');
let tagElements = document.getElementsByClassName('article_tags');
function consolePop(text) {
    let popDiv = document.createElement('div');
    popDiv.id="console_msg_div"
    popDiv.innerHTML = `<div id="console_msg">${text}</div>`;
    document.body.prepend(popDiv);
    let popDivMsg = document.getElementById('console_msg');
    popDivMsg.style.animation = "pop-up 0.3s";
    setTimeout(()=>{
        popDivMsg.style.animation = "pop-down 0.3s";
        setTimeout(()=>{document.getElementById('console_msg_div').style.display = 'none'}, 250)
    }, 2000)
};

for(let i=0; i< tagElements.length; i++){
    if(tagElements[i].textContent){
        tagElements[i].innerHTML = tagElements[i].textContent.split(',').map(tag => {
            return `<p>${tag}</p>`
        }).slice(0, 4).join(" ");
    }
}

function openReader(){
    GridWrapper.classList.add('show_reader');
    reader.style.display = "unset";
}

function closeReader(){
    GridWrapper.classList.remove('show_reader');
    reader.style.display = "none";
}

function showArticle(title, tags, content, img){
    openReader()
    console.log(title)
    console.log(tags)
    console.log(tags.split(',').map(tag =>`<p>${tag}</p>`).join(" "))
    console.log(img)
    reader.innerHTML = `<h3 id="reader_title">${title}</h3> ${img? (`<img src="${img}" alt="${title}">`) : ""}
    <div class="article_tags">
        ${tags.split(',').map(tag =>`<p>${tag}</p>`).join(" ")}
    </div>

    <p id="reader_content">${content}</p>`;
}

searchInput.addEventListener('keypress', (e)=>{
    if (e.keyCode == 13)
    searchBtn.click();
})
searchBtn.addEventListener('click', ()=>{
    if (!searchInput.value) {
        consolePop("Error: no search query");
    }
    else{
        closeReader()
        searchBar.submit()
        console.log('hello')
    }
})