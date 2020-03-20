from json import loads

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

class Choice:
    def __init__(self):
        options = []

class Option:
    def __init__(self, name, chance):
        self.name = name
        self.chance = chance
    

def loadFromFile(fname):
    with open(fname) as f:
        data = f.read()
    
    done = False
    cur = data
    
    while not done:
        for key in cur:
            new_option = Option(key, cur[key]["chance"])



@app.route("/")
def index():
    return render_template("tree.html")

@socketio.on('ask')
def sendJSON(message):
    with open("tree.json") as f:
        data = f.read()
    emit('JSON', data) 

@socketio.on('update')
def updateJSON(message):
    with open("tree.json") as f:
        old = f.read()

    emitter = message["data"]["from"]

    old = loads(old)

    cur = old
    cur_chance = 1
    for count, i in enumerate(emitter):
        if (count != len(emitter)):
            cur_chance *= cur[emitter[i]]["chance"]
            cur = cur[emitter[i]]["enfants"]
    print(cur_chance)
    emit('answer', cur_chance)



@socketio.on("add")
def addJSON(message):
    path = message["data"]["parent"]
    print(path)


def find_key(d, value):
    for k,v in d.items():
        if isinstance(v, dict):
            p = find_key(v, value)
            if p:
                return [k] + p
        elif v == value:
            return [k]

if __name__ == '__main__':
    socketio.run(app, debug=True)