from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit
#from codenames import game

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')

@socketio.on('drive')
def on_drive(data):
    """Drive"""
    print(data)

@socketio.on('radar')
def on_radar(data):
    """Radar"""
    for x in range(6):
        emit('radar', {'angle': x})



if __name__ == '__main__':
    socketio.run(app, debug=True)