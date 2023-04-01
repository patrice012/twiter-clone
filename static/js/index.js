// toggle list view

document.addEventListener("DOMContentLoaded", (e) => {
    console.log(e);

    var start = setTimeout(()=>{
        var navTweet = document.getElementById("tweet-nav");
        console.log(navTweet, 'start loading');
        navTweet.classList.add("onload");
    }, 500)
});

 var start = setTimeout(()=>{
        var navTweet = document.getElementById("tweet-nav");
        console.log(navTweet, 'loading state');
        navTweet.classList.add("onload");
    }, 500)
