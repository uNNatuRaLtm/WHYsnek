import os,math, sys
import numpy as np
from flask import Flask, request, jsonify
from timeit import default_timer as timer #del later

app = Flask(__name__)

# a method to dig json
def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result

# because it won't just print()  to console like that
def sho(x):
    print(x, file=sys.stderr)


# the webhooks
@app.route("/start", methods=["POST"])
def start():
    data = request.get_json()
    
    return jsonify(
        color = "#e3c3d3",
        name = "Hunter",
        taunt = "better now?!",
        head_type = "fang",
        tail_type = "regular",
        secondary_color = "#f4f4f0",
    )

@app.route("/move", methods=["POST"])
def move():
    start = timer() # Del later
    # Could make things easier with namedtuple and object_hook but time is precious
    data = request.get_json()
    # Delete intermediate variables later wherever possible
    food = data.get("food") 

    w = data.get("width")
    h = data.get("height")
    snakes = data.get("snakes")["data"] # List of dicts
    mySnake = data.get("you")

    # My body
    myBod = list(zip(find('x',mySnake),find('y',mySnake)))

    # My head 
    hx, hy = myBod[0] 
    
    # Foods
    food_points = list(zip(find('x',food),find('y',food)))

    # Snakes
    snake_points = list(zip(find('x',snakes),find('y',snakes)))

    goNext = ['up','right','down','left']
    
    # Make grid with edges (w+2)x(h+2) with survival score (-1 is ded?) and implement basic constraints
    # Right now we're plotting the whole grid but this is not required! Only the possibilities need scores. (one is always -1)

    board = np.zeros((h+2,w+2))
    board[0] = -1
    board.T[0] = -1
    board.T[w+1] = -1
    board[h+1] = -1

    # Scores are context dependent (defined as behaviours like grow, chill, kill)
    if mySnake["health"] > 90:
        food_reward = 0
    elif mySnake["health"] > 70:
        food_reward = 0.5
    elif mySnake["health"] > 50:
        food_reward = 1
    elif mySnake["health"] > 20:
        food_reward = 4
    # Scores given to +events can be varied later to tune behaviour
    
    for x,y in food_points:
        board[y,x] += (math.fabs(x-hx)+math.fabs(y-hy)+2)*food_reward # Scale by Manhattan distance

    for x,y in snake_points:
        board[y,x] = -1

    # Later try ?vector fields? .. many steps of free space ahead is same but closed/walled-off spaces get exponentially worse.
    # Later try heading to corners?

    # Decision time!

    decision = space.index(max(board[hy,hx+1], board[hy+1,hx+2], board[hy+2,hx+1], board[hy+1,hx]))
    ##
    end = timer() # Del later
    sho("RUNTIME: {0}ms. MAX 200ms, currently using {1}%".format(((end - start) * 1000),(((end - start) * 1000) / 2)))
    ##
    
    return jsonify(
        move = goNext[decision],
        taunt = msg
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
