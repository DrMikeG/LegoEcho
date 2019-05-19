var audio;
var distance;
var pingN = 0;

document.addEventListener("DOMContentLoaded", function () {

    audio  = document.getElementById("play");
    distance = document.getElementById("distance");
});

function playSound () {
    if (audio !== undefined)
        audio.play();
    
    pingN+=1;

    if (distance !== undefined)
        distance.textContent = ("Ping! : " + pingN); 

}