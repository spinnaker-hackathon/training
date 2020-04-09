# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os, random

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

username = os.getenv('RPS_USER', "RPS Master")
version = os.getenv('RPS_VERSION', "alpha")

@app.route('/')
def hello():
    print (username)
    print (version)
    return render_template('index.html', version=version, username=username) 

@app.route('/compete')
def compete():
    print (username)
    print (version)
    playerGesture = gestureMap(request.args.get('gesture', random.randint(0, 2), type=int))
    print (playerGesture)
    computerGesture = gestureMap(random.randint(0, 2))
    print (computerGesture)
    winner = whoWon(playerGesture, computerGesture, username)
    print (winner)
    return render_template('results.html', version=version, username=username, playerGesture = gestureIcon(playerGesture), computerGesture = gestureIcon(computerGesture), winner = winner)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify(ping="pong!")

def gestureMap(gestureIndex):
    gestures = {
        0: "rock",
        1: "paper",
        2: "scissors",
    }
    return gestures.get(gestureIndex, "foul")

def gestureIcon(gesture):
    gestureIcons = {
        "rock": "👊",
        "paper": "🖐",
        "scissors": "✌️"
    }
    return gestureIcons.get(gesture, "🧨")

def whoWon(playergesture, computergesture, playername):
    winner = "no one"
    if (playergesture == "rock"):
        if (computergesture == "paper"):
            winner = "computer"
        elif (computergesture == "scissors"):
            winner = playername
    elif (playergesture == "paper"):
        if (computergesture == "rock"):
            winner = playername
        if (computergesture == "scissors"):
            winner = "computer"
    else:
        if (computergesture == "rock"):
            winner = "computer"
        elif (computergesture == "paper"):
            winner = playername
    return winner



if __name__ == '__main__':
    rpswebport = os.getenv('RPSWEB_PORT', 80)
    app.run(debug=True, host='0.0.0.0', port=rpswebport)