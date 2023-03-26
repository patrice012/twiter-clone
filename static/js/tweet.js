const contentInput = document.getElementById("id_content");
const contentDiv = document.getElementById("tweet_content");

// switch the current value for the content input and the custom div content editable
if (contentDiv) {
  contentDiv.addEventListener("input", switchContent);
}

// befor update fill the current value to content input to the content div editable
const updatePostContent = document.querySelector(".update_post");
// if (updatePostContent) {
//   contentDiv.textContent = contentInput.value;
// }


// switch content

function switchContent(e) {
  let currentEle = e.target;
  switch (e.target.attributes.name.textContent) {
    case "create_tweet":
      switchEle = contentInput;
      break;

    // case "create_tweet":
    //   switchEle = switchShare;
    //   break;

    // case "comment_post":
    //   switchEle = switchComment;
    //   break;
  }
  switchText(currentEle, switchEle);
}

function switchText(currentEle, switchEle) {
  switchEle.value = currentEle.textContent;
  return switchEle.value;
}