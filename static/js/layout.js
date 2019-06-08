const navslide = ()=>
{
    var nav = document.querySelector("nav");
    var hamburger = document.querySelector(".hamburger");
    hamburger.addEventListener("click", ()=>
    {
        nav.classList.toggle("nav-active");
    });
}

const activelink = ()=>
{
    var activeLinkId = document.getElementsByName("active-link")[0].getAttribute("value");
    if(activeLinkId!=null)
    console.log(activeLinkId)
    document.getElementById(activeLinkId).classList.add("active-li")
}
activelink();
navslide();