var socket;

(function connect() {
    socket = io.connect('http://' + document.domain + ':' + location.port);
    // verify our websocket connection is established
})();

socket.on('connect', function() {
    console.log('Websocket connected!');
});

socket.on('radar', function(msg) {
    console.log(msg.angle);
});

function driveFwd() {
  console.log('Drive FWD');
  socket.emit('drive', {speed: 'really fast'});
}

function radar() {
  console.log('radar');
  socket.emit('radar', {});
}