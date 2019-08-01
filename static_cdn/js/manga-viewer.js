let images = document.querySelectorAll(".content-image")
let activeImageNumber = 0;
let totalImages = images.length-1;
let pageNumber = document.querySelector("#pageNumber");

let nextPageBtns = document.querySelectorAll("#nextPageBtn");
let prevPageBtns = document.querySelectorAll("#prevPageBtn");

function nextPage()
{
    if(activeImageNumber>= totalImages)
        return;
    
    images[activeImageNumber].classList.remove("active-image");
    images[++activeImageNumber].classList.add("active-image");
    pageNumber.innerHTML = "Page " +(activeImageNumber+1);

}

function prevPage()
{
    if(activeImageNumber <= 0)
    return;

    images[activeImageNumber].classList.remove("active-image");
    images[--activeImageNumber].classList.add("active-image");
    pageNumber.innerHTML = "Page " + (activeImageNumber+1);
}

nextPageBtns.forEach((btn)=>
{
    btn.addEventListener("click", nextPage);
});

prevPageBtns.forEach((btn)=>
{
    btn.addEventListener("click", prevPage);
});
