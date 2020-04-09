from flask import Flask
from flask import request
import os
import random

app = Flask(__name__)

@app.route('/')
def hello():
    os.environ['RPS_USER'] = 'username'
    playgame = '<p><br><a href="compete?gesture=1">play game</a>'
    return '<html><title>RPS</title><body><h1>Hey, we have Flask in a Docker container!</h1>' + playgame + '<p>RPSWEB_PORT: ' + os.getenv('RPSWEB_PORT') + '</body></html>'

@app.route('/compete')
def compete():
    gesture = gestureMap(request.args.get('gesture', random.randint(0, 2), type=int))
    print (gesture)
    computergesture = gestureMap(random.randint(0, 2))
    return "<html><title>RPS</title><body><h3>You played : " + gesture + "<br> Computer played: " + computergesture + "<br><br>Result: " + whoWon(gesture, computergesture) + " won </h3></body></html>"

def gestureMap(gestureIndex):
    gestures = {
        0: "rock",
        1: "paper",
        2: "scissors",
    }
    return gestures.get(gestureIndex, "foul")

def whoWon(playergesture, computergesture):
    winner = "no one"
    if (playergesture == "rock"):
        if (computergesture == "paper"):
            winner = "computer"
        elif (computergesture == "scissors"):
            winner = "you"
    elif (playergesture == "paper"):
        if (computergesture == "rock"):
            winner = "you"
        if (computergesture == "scissors"):
            winner = "computer"
    else:
        if (computergesture == "rock"):
            winner = "computer"
        elif (computergesture == "paper"):
            winner = "you"
    return winner



if __name__ == '__main__':
    rpswebport = os.getenv('RPSWEB_PORT', 80)
    app.run(debug=True, host='0.0.0.0', port=rpswebport)