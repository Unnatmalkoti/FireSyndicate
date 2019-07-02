const leftBtn = document.querySelector("#left-arrow");
const rightBtn = document.querySelector("#right-arrow");

const sliderContent = document.querySelector(".slider-content");
const slides = document.querySelectorAll(".slide");

let counter =0;

slides.forEach((slide)=>
{
    if(slide.getAttribute("order")< 0)
    counter++;
})

sliderContent.style.transform = "translateX(-" + 100*counter +"% )";



rightBtn.addEventListener("click", function()
{
    sliderContent.style.transition = "transform 0.6s ease-in-out";
    if(counter >= slides.length -1 )
        return;
    counter++;
    sliderContent.style.transform = "translateX(-" + 100*counter +"% )";
})

leftBtn.addEventListener("click", function()
{
    sliderContent.style.transition = "transform 0.6s ease-in-out";
    if(counter <= 0 )
    return;
    counter--;
    sliderContent.style.transform = "translateX(-" + 100*counter +"% )";

})