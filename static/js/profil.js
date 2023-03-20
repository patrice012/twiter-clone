let imgLinks = document.querySelectorAll('div.form__field > a[href^="/media/"]');


if (imgLinks){
    Array.from(imgLinks).forEach((img) => {
        img.previousElementSibling.classList.add("selecteMedia");
    });
}


let imgLink = document.querySelectorAll('div.form__field > a[href^="/media/"] ~ br');

if (imgLink){
    Array.from(imgLink).forEach(ele => {
        ele.nextSibling.textContent = "";
    })
}

// preview image onload


let formField = document.querySelectorAll(".form__field");
let arrFormField = Array.from(formField)
arrFormField.forEach(ele => {
    ele.addEventListener('change',previewImage)
})

function previewImage(){
        let previewCard = this.querySelector('img')
        let previewFile = this.querySelector('[type="file"]').files[0];
        if(previewFile && previewCard){
            let reader = new FileReader();
            reader.addEventListener('load',()=> {
                previewCard.src = reader.result
            });

            reader.readAsDataURL(previewFile)
        }
}



