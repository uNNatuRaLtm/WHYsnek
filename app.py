import os,math, sys
from flask import Flask, request, jsonify
from timeit import default_timer as timer

app = Flask(__name__) #App is now an instance of Flask.

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
# because it won't just print to console like that
def sho(x):
    print(x, file=sys.stderr)

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
    start = timer() #NOTE THIS IS OUR TIMER START POINT
    data = request.get_json()
    food = data.get("food") #Array
   
    #game_id = data.get("game_id")
    height = data.get("height")
    snakes = data.get("snakes") #Array
    #dead_snake = data.get("dead_snake") #array
    #turn = data.get("turn")
    width = data.get("width")
    
    mySnake = data.get("you")
    #NOTE grid_options[0] = general_grid // grid_options[1] = food_grid
    grid_options = controller.grid_setup(food, width, height, snakes, mySnake["length"])

 

    #NOTE Now, set our coordinates!
    myBod = list(zip(find('x',mySnake),find('y',mySnake)))
    hx, hy = myBod[0]

    #NOTE Search for the coordinates of the closest target if health < hunger_thres, ex 80
    target = controller.get_closest_food(grid_options[1], hx, hy)
    msg = """I'm hungry!!"""
    if mySnake["health"]>50:
        if len(grid_options[2])>=3:
            target = controller.get_closest_food(grid_options[2], hx, hy)
            msg = 'I want to be your friend!'

    #NOTE Get the next move based on the pellet
    next_move = controller.get_move(grid_options, target, hx, hy, height, width)

    #NOTE This is the end reference point of the timer. Just to get a good idea of what the runtime of the program is in total
    end = timer()
    sho("RUNTIME: {0}ms. MAX 200ms, currently using {1}%".format(((end - start) * 1000),(((end - start) * 1000) / 2)))

    #NOTE Return the move in the JSON object wrapper
    return jsonify(
    move = next_move, #NOTE This is what controls where the snake goes!
    taunt = msg
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
