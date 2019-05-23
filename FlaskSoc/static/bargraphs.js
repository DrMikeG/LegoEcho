var canvas;
var context;
var step = -100;

// Get a regular interval for drawing to the screen
window.requestAnimFrame = (function (callback) {
    return window.requestAnimationFrame ||
        window.webkitRequestAnimationFrame ||
        window.mozRequestAnimationFrame ||
        window.oRequestAnimationFrame ||
        window.msRequestAnimaitonFrame ||
        function (callback) {
            window.setTimeout(callback, 1000 / 60);
        };
})();

// Draw to the canvas
function renderCanvas() 
{
    step+=1;
    if (step > 100)
        step = -100;

    renderRing();
}

function renderRing() {

    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
    
    var width = canvas.width;
    var height = canvas.height;
    //console.log("width ",width);
    //console.log("height ",height);

    var midWidth= width /2;
    
    var grdL = context.createLinearGradient(0, 0, midWidth,height );
    grdL.addColorStop(0, "green");
    grdL.addColorStop(0.8, "#004400");
    grdL.addColorStop(1, "#000000");
    // Fill with gradient
//    context.fillStyle = grdL;
    //context.fillRect(0, 0, midWidth, height);

    var grdR = context.createLinearGradient(midWidth, 0, width,height );
    grdR.addColorStop(0, "#000000");
    grdR.addColorStop(0.2, "#440000");
    grdR.addColorStop(1, "red");
    // Fill with gradient
 //   context.fillStyle = grdR;
//    context.fillRect(midWidth, 0, midWidth, height);

    //context.lineWidth = 5;
    
    //context.strokeRect(0, 0, width, height);

    // How many boxes
    var nBoxesInHalf = 10;
    var boxWidthAndPadding = (midWidth / 10);
    var padding = 2;
    var halfPadding = (padding/2);
    var boxLineWidth = 2;
    // distance between the middle of each box...
    var boxWidth = boxWidthAndPadding - (padding + (2*boxLineWidth));    
    // Start from the middle...

    context.lineWidth = 5;
    context.strokeStyle = "#000000";
    context.fillStyle = grdL;


    // step  varies between -100 and 100;
    // map speed to 0 and 10 left
    var lBox = 0;
    if (step < 0)
    {
        // How many left boxes do we want
        lBox = (-step/100) * nBoxesInHalf;
    }
    var rBox = 0;
    if (step > 0)
    {
        // How many right boxes do we want
        rBox = (step/100) * nBoxesInHalf;
    }

    for (var l=0; l < nBoxesInHalf; l++)
    {
        if ( l >= lBox)
            continue;
        var m = (midWidth-boxWidth-(2*padding)) -(l*boxWidthAndPadding);
        context.strokeRect(m, halfPadding, boxWidth, height-padding);        
        context.fillRect(m, halfPadding, boxWidth, height-padding);        
    }
    context.fillStyle = grdR;
    for (var r=0; r < nBoxesInHalf; r++)
    {
        if ( r >= rBox)
            continue;
        var m2 = (midWidth+padding-(2*padding))+ (r*boxWidthAndPadding);
        context.strokeRect(m2, halfPadding, boxWidth, height-padding);
        context.fillRect(m2, halfPadding, boxWidth, height-padding);
    }
    /*
    
    // 0% draw nothing
    
    console.log(step);

    for (var l=0; l < nBoxesInHalf; l++)
    {
        var m = -boxWidth + (midWidth-(l*boxWidthAndPadding));
        context.strokeRect(m, padding, boxWidth, height-padding);
        if (speedPCT > 0)
        {
            // If speed is positive, fill left boxes
            context.fillRect(m, padding, boxWidth, height-padding);
        }    
    }
    for (var r=0; r < nBoxesInHalf; r++)
    {
        var m2 = boxWidth + (midWidth+(r*boxWidthAndPadding));
        context.strokeRect(m2, padding, boxWidth, height-padding);

        

    }
    */


}


document.addEventListener("DOMContentLoaded", function () {

    canvas = document.getElementById("bargraph-canvas1");
    context = canvas.getContext("2d");

    (function drawLoop() {
        requestAnimFrame(drawLoop);
        renderCanvas();
    })();

}, false);
