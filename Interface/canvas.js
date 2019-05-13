var canvas;
var context;

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

function drawTick(x, y, radiusStart, length, width, angle, colour) {

    var rAngle = (angle / 360.0) * 2 * Math.PI;

    context.beginPath();
    // +Y is down the canvas?
    var cosXStart = x + (radiusStart * Math.cos(rAngle));
    var cosYStart = y - (radiusStart * Math.sin(rAngle));

    var cosXEnd = x + ((radiusStart + length) * Math.cos(rAngle));
    var cosYEnd = y - ((radiusStart + length) * Math.sin(rAngle));

    context.moveTo(cosXStart, cosYStart);
    context.lineTo(cosXEnd, cosYEnd);
    context.strokeStyle = colour;
    context.lineWidth = width;
    context.closePath();
    context.stroke();
}
function drawTicks(x, y, radiusStart) {
    for (var i = 0; i < 36; i++) {
        var angle = i * 10;
        drawTick(x, y, radiusStart, 20, 3, angle, "#519b48");
    }

}

function renderRing() {

    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
    

    context.clearRect(0, 0, canvas.width, canvas.height);

    var width = canvas.width;
    var height = canvas.height;

    var circle = {
        x: width / 2,
        y: height / 2,
        od: (0.75 * width / 2)
    };

    for (var i = 10; i > 0; i--) {
        drawCircle(circle.x, circle.y, i * 0.1 * circle.od, 3, "#519b48", "#000000");
    }

    drawTicks(circle.x, circle.y, circle.od);

}


// Set up mouse events for drawing
var drawing = false;
var mousePos = { x: 0, y: 0 };
var lastPos = mousePos;

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


// Draw to the canvas
function renderCanvas() {

    renderRing();

    var touchSize = 50;
    // is fully within ring?
    if (drawing && isPositionWithinRing(canvas, mousePos, touchSize)) {
        var context = canvas.getContext("2d");
        //console.log("Drawing circle at", mousePos);
        drawCircle(context, mousePos.x, mousePos.y, 50, 3, "red", "#000000");
    }


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

    canvas = document.getElementById("html-canvas");
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
        lastPos = getMousePos(e);
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