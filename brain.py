import numpy as np
import sys
# because it won't just print()  to console like that
def sho(x):
    print(x, file=sys.stderr)

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

def decide(data):
    food = data.get("food")
    w = data.get("width")
    h = data.get("height")
    snakes = data.get("snakes")["data"]
    mySnake = data.get("you")
    myBod = list(zip(find('x',mySnake),find('y',mySnake)))
    hx, hy = myBod[0]
    food_points = list(zip(find('x',food),find('y',food)))
    sho('Food at: '+str(food_points))
    

    # Make grid with edges (w+2)x(h+2) with survival score (-1 is ded?) and implement basic constraints
    # Right now we're plotting the whole grid but this is not required! Only the possibilities need scores. (one is always -1)

    board = np.zeros((h+2,w+2))
    board[0] = -1
    board.T[0] = -1
    board.T[w+1] = -1
    board[h+1] = -1

    for snake in snakes:
        for x,y in zip(find('x',snake),find('y',snake)):
            board[y+1,x+1] = -1
            if snake != mySnake:
                board[y,x+1] = -0.5 * (snake["length"] - mySnake["length"])
                board[y+2,x+1] = -0.5 * (snake["length"] - mySnake["length"])
                board[y+1,x] = -0.5 * (snake["length"] - mySnake["length"])
                board[y+1,x+2] = -0.5 * (snake["length"] - mySnake["length"])


    # Scores can be context dependent (defined as behaviours like grow, chill, kill)
    if mySnake["health"] > 90:
        food_reward = 0
    elif mySnake["health"] > 70:
        food_reward = 0.3
    elif mySnake["health"] > 50:
        food_reward = 1
    elif mySnake["health"] > 20:
        food_reward = 5
    else:
    	food_reward = 10
    # Scores given to +events can be varied later to tune behaviour

    for x,y in food_points:
        board[y+1,x+1] = food_reward # * (math.fabs(x-hx)+math.fabs(y-hy)+2)



    board[hy+1,hx+1] = -5
    # Later try ?? many steps of free space ahead is same but closed/walled-off spaces get exponentially worse.
    # Later try heading to corners?

    # Decision time!
    # Raw value
    space = [board[hy,hx+1], board[hy+1,hx+2], board[hy+2,hx+1], board[hy+1,hx]]

    # Give line of smell-
    space = list(map(lambda a,b:a+np.mean(b), space, [board[:hy+1,hx+1],board[hy+1,hx+2:],board[hy+2:,hx+1],board[hy+1,:hx+1]]))

    # Give randomness
    space = list(map(lambda a,b:a+b/2, space,np.random.rand(4)))

    sho(board)
    decision = space.index(max(space))

    return decision
