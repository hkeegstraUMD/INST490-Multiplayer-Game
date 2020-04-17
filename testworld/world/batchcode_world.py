from evennia import create_object, search_object
from typeclasses import rooms, exits

entrance = create_object(rooms.Room, key ="entrance")
puzzle1 = create_object(rooms.Room, key = "puzzle1")
goal = create_object(rooms.Room, key = "exit")

entrance.db.desc = """
The entrance to the dungeon. Here, players find the artifacts that give them insight.
There is a door to the north leading to another chamber
"""

entrance_puzzle1 = create_object(exits.Exit, key="north", aliases =["n"], 
                                location =entrance, destination = puzzle1)

puzzle1.db.desc = """
The first puzzle room. Players will work together to solve the puzzle and get out.
The door to the south remains open. There is a door to the north that will open when the puzzle is solved.
"""
puzzle1_entrance = create_object(exits.Exit, key="south", aliases =["s"], 
                                location =puzzle1, destination = entrance)
puzzle1_goal = create_object(exits.Exit, key="north", aliases =["n"], 
                                location =puzzle1, destination = goal)

goal.db.desc = """
After solving all the puzzles, the players have reached the goal.
Players may complete the game here, but the door back south remains open.
"""
puzzle_entrance = create_object(exits.Exit, key="south", aliases =["s"], 
                                location =goal, destination = puzzle1)

limbo = search_object('Limbo')[0]
limbo_exit = create_object(exits.Exit, key = "enter world", aliases =["enter"],
                            location = limbo, destination = entrance)