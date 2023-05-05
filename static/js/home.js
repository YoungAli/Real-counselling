const faqTiles = document.getElementsByClassName('faq-tiles');

const faqAnsTile = document.querySelector('#faq-ans-tile');

const faqAnswers = {
'0':"Counseling is a process that involves talking with a trained professional who can provide support, guidance, and feedback on personal and emotional issues.",
'1':'Counseling can help with a wide range of issues, including anxiety, depression, relationship problems, grief and loss, addiction, self-esteem, and more.',
'2':"The length of counseling varies depending on the individual's needs and goals. Some people may benefit from short-term counseling that lasts a few weeks or months, while others may require more long-term support.",
'3':"During a counseling session, the therapist will listen to the individual's concerns, provide feedback and guidance, and help the person develop coping strategies and solutions to their problems.",
'4':"Yes, counseling is confidential, and the therapist will not share any information with others unless the individual gives permission or there is a safety concern.",
'5':"There are many ways to find a counselor, including through personal recommendations, online directories, or contacting a mental health clinic or professional organization.",
'6':"The cost of counseling varies depending on the provider, location, and type of counseling. Many therapists offer sliding-scale fees or accept insurance.",
'7':"It is important to feel comfortable and safe with your counselor. If you don't feel a connection, it is okay to try a different therapist who may be a better fit for your needs."
}
 
for (let i = 0; i < faqTiles.length; i++) {
    faqTiles[i].addEventListener('click', ()=>{
        setTimeout(()=>{
            faqAnsTile.textContent = faqAnswers[i]
        }, 250);
        faqAnsTile.style.animation = 'flicker 0.5s';
        setTimeout(()=>{
            faqAnsTile.style.animation = 'none';
        }, 500)
        
    })
}