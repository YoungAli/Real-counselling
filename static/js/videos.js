const vidArea = document.querySelector('#video_results');
const searchBtn = document.querySelector('#search_btn');
const searchInput = document.querySelector('#search_input');

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

        async function fetchVids(isScrolling) {
            let randomKeywords = ['anxiety', 'relationship', 'career', 'addiction','education', 'anger', 'christian', 'spiritual'].sort(() => 0.5 - Math.random()).slice(0, 4).join();

            let response = await fetch(`https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId=UCq2ueL6wl7slTuInRbFpe7w&maxResults=5&q=${searchInput.value? searchInput.value : randomKeywords}&videoEmbeddable=true&type=video&key=AIzaSyA4H_W3S25Jkov2f5uKxsjm_Vgmlz4Sv58`);

            let results = await response.json();
            
            let videos;

            if (results.items.length) {
                videos = await results.items.map(video => {
                    return `<div class="video-wrapper">
                        <hr>
                        <p class="vid_title">${video.snippet.title}</p>
                        <iframe src="https://www.youtube.com/embed/${video.id.videoId}"></iframe>
                        <p class="vid_desc">${video.snippet.description}</p>
                    </div>`
                }).join(' ');
            } else{
                consolePop(`<a href="http://127.0.0.1:8000/videos">No search result, click to go back</a>`, 'infinite');

                vidArea.style.display = 'none';
                document.querySelector('#vid_preloader').style.display = 'none';
            }

            if (isScrolling) {
                // vidArea.innerHTML += videos;
                let newVideos = document.createElement('div');
                videos.replace(`<div class="video-wrapper">`, ` `);
                videos.replace(`</div>`, ` `);
                newVideos.classList.add('video-wrapper');
                newVideos.innerHTML = videos;
                vidArea.append(newVideos);
            }
            else{
                vidArea.innerHTML = videos;
            }

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
                fetchVids(false);
            }
        })
        fetchVids(false);

        document.addEventListener('scroll', () => {
        if (window.scrollY >= (document.documentElement.scrollHeight - window.innerHeight)) {
            fetchVids(true);
        }
    })