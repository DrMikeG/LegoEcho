from flask import Flask
app = Flask(__name__)

#https://secdevops.ai/weekend-project-part-2-turning-flask-into-a-real-time-websocket-server-using-flask-socketio-ab6b45f1d896

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()