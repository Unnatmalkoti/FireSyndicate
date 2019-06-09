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
    var active_tab =document.getElementById(activeLinkId);
    active_tab.classList.add("active-li");
    var nav_ul = document.getElementsByTagName("nav")[0].firstElementChild;
    nav_ul.addEventListener("mouseover", ()=>active_tab.classList.remove("active-li"));
    nav_ul.addEventListener("mouseout", ()=>active_tab.classList.add("active-li"));

}

const goto = (link)=>
{
    window.location= link;
}

//Touch response goes here
var nav = document.querySelector("nav");
var body = document.querySelector("body");
var touchstartX;
nav.addEventListener("touchstart",(event)=>{
    touchstartX =event.touches[0].pageX;

    console.log(event.touches[0]);
});
var change;
body.addEventListener("touchstart",(event)=>{
    touchstartX =event.touches[0].pageX;
    change =0;
    console.log('body');
});


nav.addEventListener("touchmove",(event)=>{
     change = event.touches[0].pageX- touchstartX ;
     console.log(change);
    if(nav.classList.contains("nav-active") && change <0)
        nav.style.transform = `translate(${change}px)`;
});

body.addEventListener("touchmove",(event)=>{
    change = event.touches[0].pageX- touchstartX ;
    console.log(change);
   if(!nav.classList.contains("nav-active") && change < 250 && change >0)
       nav.style.transform = `translate(${change-250}px)`;
});

nav.addEventListener("touchend",(event)=>{
    if(change > -100)
        nav.classList.add("nav-active");
    if(change < -100)
        nav.classList.remove("nav-active");
    nav.style.removeProperty('transform');
});

body.addEventListener("touchend",(event)=>{
    if(change > 100)
        nav.classList.add("nav-active");
    if(change < 100)
        nav.classList.remove("nav-active");
    nav.style.removeProperty('transform');
});






activelink();
navslide();