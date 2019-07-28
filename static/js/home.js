






function slider()
{
    let counter =0;
    const leftBtn = document.querySelector("#slider-left-arrow");
    const rightBtn = document.querySelector("#slider-right-arrow");

    const sliderContent = document.querySelector(".slider-content");
    const slides = document.querySelectorAll(".slide");


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

}

function blogSlider()
{
    const leftBtn = document.querySelector("#blog-left-arrow");
    const rightBtn = document.querySelector("#blog-right-arrow");

    let counter =0;
   

    const sliderContent = document.querySelector(".post-content");
    const slides = document.querySelectorAll(".post-tile");

    rightBtn.addEventListener("click", function()
    {
        sliderContent.style.transition = "transform 0.6s ease-in-out";
        if(counter >= slides.length -1 )
            return;
        let multiplier = Math.floor(document.querySelector(".post-content").offsetWidth / 490)
        counter = counter + multiplier;
        sliderContent.style.transform = "translateX(-" + 475*counter +"px )";
        
    })

    leftBtn.addEventListener("click", function()
    {
        sliderContent.style.transition = "transform 0.6s ease-in-out";
        if(counter <= 0 )
            return;
        let multiplier = Math.floor(document.querySelector(".post-content").offsetWidth / 490)
        counter = counter - multiplier;
        sliderContent.style.transform = "translateX(-" + 475*counter +"px )";

    })

}
try
{
    slider();
}catch{}
try
{
    blogSlider();
}catch{}

