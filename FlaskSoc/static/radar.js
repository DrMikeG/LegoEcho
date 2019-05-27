var canvas;
var context;
var control = { x: 0, y: 0, od: 50};

var drawing = false;
var mousePos = { x: 0, y: 0 };
var lastPos = mousePos;

var sweepAngle = 0;


function drawTick(length, width, angle, colour) {

    var rAngle = (angle / 360.0) * 2 * Math.PI;

    context.beginPath();
    // +Y is down the canvas?
    var cosXStart = control.x + (control.od * Math.cos(rAngle));
    var cosYStart = control.y - (control.od * Math.sin(rAngle));

    var cosXEnd = control.x + ((control.od + length) * Math.cos(rAngle));
    var cosYEnd = control.y - ((control.od + length) * Math.sin(rAngle));

    context.moveTo(cosXStart, cosYStart);
    context.lineTo(cosXEnd, cosYEnd);
    context.strokeStyle = colour;
    context.lineWidth = width;
    context.closePath();
    context.stroke();
}

function drawTicks() 
{
    for (var i = 0; i < 36; i++) {
        var angle = i * 10;
        drawTick(20, 3, angle, "#519b48");
    }
}

function drawCircle(x, y, radius, border, border_colour, fill_colour) {
    context.beginPath();
    context.arc(x, y, radius, 0, 2 * Math.PI);
    context.strokeStyle = border_colour;
    context.fillStyle = fill_colour;
    context.lineWidth = border;
    context.closePath();
    context.fill();
    context.stroke();
}

function renderRing() {

    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
    
    context.clearRect(0, 0, canvas.width, canvas.height);

    var width = canvas.width;
    var height = canvas.height;

    control.x = width / 2;
    control.y = height / 2;
    control.od = (0.75 * width / 2);

    for (var i = 10; i > 0; i--) {
        drawCircle(control.x, control.y, i * 0.1 * control.od, 3, "#519b48", "#000000");
    }

    drawTicks();

}

function renderSweep() 
{
    var rAngleA = (sweepAngle / 360.0) * 2 * Math.PI;
    var rAngleB = ((sweepAngle+20) / 360.0) * 2 * Math.PI;

    context.beginPath();
    
    var cosXStart = control.x + (control.od * Math.cos(rAngleA));
    var cosYStart = control.y - (control.od * Math.sin(rAngleA));

    var cosXEnd = control.x + (control.od * Math.cos(rAngleB));
    var cosYEnd = control.y - (control.od * Math.sin(rAngleB));

    context.strokeStyle = "#FF0000";
    context.arc(control.x, control.y, control.od, rAngleA, rAngleB);
    context.lineTo(control.x, control.y);
    context.closePath();
    context.stroke();
}

function renderTouch()
{
    var touchSize = 50;
    // is fully within ring?
    if (drawing ) {
     
        var toDraw = mousePos;
        if (isPositionWithinRing(toDraw, touchSize))
        {
            drawCircle(toDraw.x, toDraw.y, 30, 3, "red", "#000000");
        }
        else
        {    
            projectPositionWithinRing(toDraw, touchSize);
            drawCircle(toDraw.x, toDraw.y, 30, 3, "red", "#000000");
        }
    }
}

// Draw to the canvas
function renderCanvas() 
{

    renderRing();

    sweepAngle += 1;
    if (sweepAngle > 360)
        sweepAngle = 0;
    renderSweep();

    renderTouch();
    
}


// Set up mouse events for drawing

// Get the position of a touch relative to the canvas
function getTouchPos(touchEvent) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: touchEvent.touches[0].clientX - rect.left,
        y: touchEvent.touches[0].clientY - rect.top
    };
}

// Get the position of the mouse relative to the canvas
function getMousePos(mouseEvent) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: mouseEvent.clientX - rect.left,
        y: mouseEvent.clientY - rect.top
    };
}

function isPositionWithinRing(mousePos, touchSize) {
    var width = canvas.width;
    var height = canvas.height;
    var circle = {
        x: width / 2,
        y: height / 2,
        od: (0.75 * width / 2)
    };
    var xDist = Math.abs(circle.x - mousePos.x);
    var yDist = Math.abs(circle.y - mousePos.y);
    var dist = Math.sqrt((xDist * xDist) + (yDist * yDist));
   return (dist + (0.5 * touchSize)) < circle.od;
}

function projectPositionWithinRing(mousePos, touchSize) {
    
    // We are assuming that mousePos is not in the ring.
    // Using similar triangles, we can scale the x and y to get to a point on the edge of the ring.

    // 
    var width = canvas.width;
    var height = canvas.height;
    var circle = {
        x: width / 2,
        y: height / 2,
        od: (0.75 * width / 2)
    };
    var xDist = Math.abs(circle.x - mousePos.x);
    var yDist = Math.abs(circle.y - mousePos.y);
    var dist = Math.sqrt((xDist * xDist) + (yDist * yDist));
    var distIncTouch = dist + (0.5 * touchSize);
    // distIncTouch > circle.od
    var scaleFactor = circle.od / distIncTouch;
    var scaledXDist = xDist * scaleFactor;
    var scaledYDist = yDist * scaleFactor;
    
    var xFactor = (circle.x - mousePos.x) > 0 ? -1 : 1;
    var yFactor = (circle.y - mousePos.y) > 0 ? -1 : 1;
    mousePos.x = (circle.x + (xFactor*scaledXDist));
    mousePos.y = (circle.y + (yFactor*scaledYDist));
}



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

// Allow for animation

// Prevent scrolling when touching the canvas

document.addEventListener("DOMContentLoaded", function () {

    canvas = document.getElementById("radar-canvas1");
    context = canvas.getContext("2d");

    document.body.addEventListener("touchstart", function (e) {
        if (e.target == canvas) {
          e.preventDefault();
        }
      }, false);
      document.body.addEventListener("touchend", function (e) {
        if (e.target == canvas) {
          e.preventDefault();
        }
      }, false);
      document.body.addEventListener("touchmove", function (e) {
        if (e.target == canvas) {
          e.preventDefault();
        }
      }, false);
    

    canvas.addEventListener("mousedown", function (e) {
        drawing = true;
        mousePos = getMousePos(e);
        //console.log("drawing at ", lastPos);
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        drawing = false;
    }, false);
    canvas.addEventListener("mousemove", function (e) {
        mousePos = getMousePos(e);
    }, false);

    // Set up touch events for mobile, etc
    canvas.addEventListener("touchstart", function (e) {
        mousePos = getTouchPos(e);
        var touch = e.touches[0];
        var mouseEvent = new MouseEvent("mousedown", {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        canvas.dispatchEvent(mouseEvent);
    }, false);
    canvas.addEventListener("touchend", function (e) {
        var mouseEvent = new MouseEvent("mouseup", {});
        canvas.dispatchEvent(mouseEvent);
    }, false);
    canvas.addEventListener("touchmove", function (e) {
        var touch = e.touches[0];
        var mouseEvent = new MouseEvent("mousemove", {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        canvas.dispatchEvent(mouseEvent);
    }, false);

    (function drawLoop() {
        requestAnimFrame(drawLoop);
        renderCanvas();
    })();

}, false);