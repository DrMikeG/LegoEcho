var socketModule = (function(){
    'use strict';

    var socket;

    (function connect() {
        socket = io.connect('http://' + document.domain + ':' + location.port);
        // verify our websocket connection is established
    })();

    var loggingObject = console;
    function GetLoggingObject(){ return loggingObject; }
    function SetLoggingObject(obj) { loggingObject = obj; }

    socket.on('connect', function() {
        GetLoggingObject().log('Websocket connected!');
    });

    socket.on('radar', function(msg) {
        GetLoggingObject().log(msg.angle);
    });

    function driveFwd() {
        GetLoggingObject().log('Drive FWD');
    socket.emit('drive', {speed: 'really fast'});
    }

    function radar() {
        GetLoggingObject().log('radar');
    socket.emit('radar', {});
    }

    return {
        radar : radar,
        driveFwd : driveFwd
    };

}());

