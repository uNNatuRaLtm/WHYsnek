import os
import numpy as np
from flask import Flask, request, jsonify
from brain import decide

app = Flask(__name__)

# a method to dig json


# the webhooks
@app.route("/start", methods=["POST"])
def start():
    data = request.get_json()
    
    return jsonify(
        color = "#e3c3d3",
        name = "JoblessSnake",
        taunt = "Seriously?!",
        head_type = "fang",
        tail_type = "regular",
        head_url = "https://avatarfiles.alphacoders.com/108/108917.png"
        secondary_color = "#f4f4f0",
    )

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    goNext = ['up','right','down','left']
    decision = decide(data)
    return jsonify(
        move = goNext[decision],
        taunt = 'msg'
    )

#log and learn?
@app.route("/end", methods=["POST"])
def end():
    data=request.get_json()
    with open("survivedTurns.txt","a") as fo:
        fo.write(str(data))




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
