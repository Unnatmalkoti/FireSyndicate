const navslide = ()=>
{
    var nav = document.querySelector("nav");
    var hamburger = document.querySelector(".hamburger");
    hamburger.addEventListener("click", (event)=>
    {   
        event.stopPropagation();
        console.log("toggled nav-active")
        nav.classList.toggle("nav-active");
        
    });
}

const dropdown = (btnClassName, menuClassName)=>
{
    var menu = document.querySelector('.'+menuClassName)
    document.querySelector('.'+btnClassName).addEventListener("click",(event)=>
    {   
            menu.classList.toggle("active-dropdown");
        event.stopPropagation();
    })
    //menu.addEventListener("click", (event)=> event.stopPropagation())
    document.querySelector("body").addEventListener("click", ()=>
    {
        menu.classList.remove("active-dropdown");
    })
}
const activelink = ()=>
{
    try
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
    catch(e)
    {
        console.log(e);
    }
}

const goto = (link)=>
{
    window.location= link;
}

//search
document.querySelector(".search-icon").addEventListener("click", function(){ document.querySelector(".search-bar").focus();});



//Touch response goes here
var nav = document.querySelector("nav");
var validTouch= true;
var body = document.querySelector("body");
var touchstartX;
nav.addEventListener("touchstart",(event)=>{
    nav.style.transition = "none" ;
    touchstartX =event.touches[0].pageX;
    event.stopPropagation();
    console.log(event.touches[0]);
});
var change;
body.addEventListener("touchstart",(event)=>{
    nav.style.transition = "none" ;
    change=0;
    touchstartX =event.touches[0].pageX;
    if (touchstartX > 50)
        validTouch=false;
    else
        validTouch=true;
    change =0;
    console.log("start X" +touchstartX);
});


nav.addEventListener("touchmove",(event)=>{
     change = event.touches[0].pageX- touchstartX ;
     console.log(change);
     event.stopPropagation();
    if(nav.classList.contains("nav-active") && change <0)
        nav.style.transform = `translate(${change}px)`;
});

body.addEventListener("touchmove",(event)=>{
    change = event.touches[0].pageX- touchstartX ;
    console.log(change);
    
    if(!nav.classList.contains("nav-active") && change < 250 && change >0 && validTouch)
        nav.style.transform = `translate(${change-250}px)`;
    if(nav.classList.contains("nav-active") && change > -250 && change <0)
        nav.style.transform = `translate(${change}px)`;
});

nav.addEventListener("touchend",(event)=>{
    
    nav.style.transition = "";
    event.stopPropagation();
    if(change > -100)
        nav.classList.add("nav-active");
    if(change < -100)
        nav.classList.remove("nav-active");
    nav.style.removeProperty('transform');
});

body.addEventListener("touchend",(event)=>{
    nav.style.transition = "";
    if(change > 50 && validTouch)
        nav.classList.add("nav-active");
    else if(change>100)
        nav.classList.add("nav-active");


    if(change < -50)
        nav.classList.remove("nav-active");
    nav.style.removeProperty('transform');
});





dropdown('accounts-icon','drop-down');
activelink();
navslide();