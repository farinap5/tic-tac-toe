from flask import Flask, render_template, request
from flask import *
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
io = SocketIO(app)

@app.route('/')
def home():
    return render_template("index.html")

# Conf = currently configuration of the game.
@io.on('jogada')
def jogada(conf):
    emit('getConf', conf,json=True, broadcast=True)

@io.on('reload')
def reload(info):
    emit('getReload',info,json=True, broadcast=True)

@io.on('sendLog')
def log(msg):
    emit('rcvLog', msg, json=True, broadcast=True)

if __name__ == "__main__":
    io.run(app, debug=True)