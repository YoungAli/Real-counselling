function showArticle(title, tags, content){
    console.log(title)
    console.log(tags)
    console.log(content)
}
let tagElements = document.getElementsByClassName('article_tags');

for(let i=0; i< tagElements.length; i++){
    if(tagElements[i].textContent){
        tagElements[i].innerHTML = tagElements[i].textContent.split(',').map(tag => {
            return `<p>${tag}</p>`
        }).slice(0, 4).join(" ");
    }
}