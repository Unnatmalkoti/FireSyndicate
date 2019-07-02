function coverSelector()
{
    var icon = document.querySelector(".icon-tray");
    var fileField = document.querySelector("#file-field");
    icon.addEventListener("click", ()=>
    {
        fileField.click();
    });

    fileField.addEventListener("input", (event)=>
    {
        var cover =document.querySelector(".comic-cover");
        // cover.style.backgroundImage = 
        var reader = new FileReader();
        reader.onload = ()=>
        {
            cover = document.getElementsByClassName("comic-cover")[0];
            cover.style.background =  'url('+reader.result+')';
            cover.style.backgroundSize =  'cover';
            cover.style.borderStyle="none";
        }
        reader.readAsDataURL(event.target.files[0]);
    });
}
coverSelector();