## A Battlesnake-2018 contender (in the process of being born)
The following is more of an About than Readme. Being written in python (using Flask), TBD soon.    

## The "Machine Learning" approach ..
.. would be if it got better over time on its own, but that needs a *LOT* of examples of games and decision feedback (which I don't have. And even if I did, wouldn't necessarily be able to implement by tomorrow.) It would also require modding the board server to continuously run games, etc, and storing histories of game states somewhere, which I don't know the most efficient way to do. (If someone could help me with that it would be awesome. Thanks!) This is analytically the optimal approach but the total number of states is larger than (humankind's best estimate of) the number of molecules in the universe, and may not be required for getting good enough solution to this problem (I hope).

So instead, I will attempt ..

## a heuristic based approach..
.. and later try to parametrize things like hunger, etc, to tweak for performance, using genetic algos if possible. This approach is basically looking at the board state and using rules-of-thumb to make decisions. Additionally, the snake can be made more sophisticated by prioritizing different rules under different circumstances (ex - hungry when low on health). Technically it would make sense to use optimal graph search algorithms to traverse the state-space, but I don't have the expertise to optimize the computation so I won't do that. Instead the attempt will be to pre-empt the best behaviour as simply as possible, by trying to have the representation be sparse/coarse informationally (ints vs floats), but higher order conceptually (abstraction++).

## Ok, so what am I doing really?

.. 
... *Surviving*, as long as possible. __Be__ the snek!
.... Wish I had enough expertize to give it an HTM brain .. but first things first.   

## Seriously though.. step by step..

1. Get the state data from the json world. Take only useful info (that you'll use to make decisions).
2. Implement constraints (short term) according to game rules. Like, don't walk into walls, or get eaten.
3. Categorize contexts ([meta - make more]) and identify current context.
4. Make decision based on current state and context.
5. Pray for the best.
6. Perhaps chuckle (at least nose exhale) at no.5 and think of ways to encode more meaning in less information. Simultaneouly consider how this game is a very good simplified case study for life and intelligence in general. Before moving to the next step, marvel at existence.
7. if (i++ > large_num): {next} else: {GOTO 3}
8. Parametrize contexts and optimize. (Did you store any data?)



