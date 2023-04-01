let contentInput = document.getElementById("id_content");
let contentDiv = document.getElementById("tweet_content");

// switch the current value for the content input and the custom div content editable
if (contentDiv) {
  contentDiv.addEventListener("input", switchContent);
}

// befor update fill the current value to content input to the content div editable
let updatePostContent = document.querySelector(".update_post");


// switch content

function switchContent(e) {
  let currentEle = e.target;
  switch (e.target.attributes.name.textContent) {
    case "create_tweet":
      switchEle = contentInput;
      break;
    }
  switchText(currentEle, switchEle);
}

function switchText(currentEle, switchEle) {
  switchEle.value = currentEle.textContent;
  return switchEle.value;
}

// remove Form after form submission

let tweetForm = document.getElementById("tweet-form");
document.addEventListener('submit',(e)=> {
    if (e.target.getAttribute('hx-post') === '/save-tweet/'){
      tweetForm.remove();
      document.querySelector('.img-preview--container').remove()
    }
    // submit
  } )


















// preview image onload

let imgBox = document.querySelector(".img-preview");
let inputImg = document.getElementById('id_tweet_picture');

if (inputImg){
  inputImg.addEventListener('change', previewImage)
}

function previewImage(e){
  let file = this.files[0];
  let reader = new FileReader()
  reader.addEventListener('load', ()=> {
    imgBox.src = reader.result
  })

  reader.readAsDataURL(file)
}