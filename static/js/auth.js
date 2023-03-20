let togglePwd = document.querySelectorAll(".lockPwd");

Array.from(togglePwd).forEach((btn) => {
  if (btn.previousElementSibling.type !== "password") {
    btn.remove();
  }
  btn.addEventListener("click", togglePwdView);
});


function togglePwdView(e){
    let ele = e.target;
    let pwdInput = e.target.previousElementSibling;
    if (pwdInput.type === "password") {
        pwdInput.type = "text";
        ele.classList.toggle("fa-lock");
        ele.classList.add("fa-unlock");

    } else if (pwdInput.type === "text"){
        pwdInput.type = "password";
        ele.classList.toggle("fa-unlock");
        ele.classList.add("fa-lock");
    }
}


