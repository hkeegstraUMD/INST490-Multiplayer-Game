from evennia import create_object, search_object
from typeclasses import rooms, exits, artifacts

entrance = create_object(rooms.Room, key ="entrance")
puzzle1 = create_object(rooms.Room, key = "puzzle1")
goal = create_object(rooms.Room, key = "exit")

entrance.db.desc = """
The entrance to the dungeon. Here, players find the artifacts that give them insight.
There is a door to the north leading to another chamber
"""

entrance_puzzle1 = create_object(exits.Exit, key="north", aliases =["n"], 
                                location =entrance, destination = puzzle1)

red_arti = create_object(artifacts.Red, key = "Red Artifact", location = entrance)
blue_arti = create_object(artifacts.Blue, key = "Blue Artifact", location = entrance)
green_arti = create_object(artifacts.Green, key = "Green Artifact", location = entrance)
yellow_arti = create_object(artifacts.Yellow, key = "Yellow Artifact", location = entrance)

puzzle1.db.desc = """
The first puzzle room. Players will work together to solve the puzzle and get out.
The door to the south remains open. There is a door to the north that will open when the puzzle is solved.
"""
puzzle1_entrance = create_object(exits.Exit, key="south", aliases =["s"], 
                                location =puzzle1, destination = entrance)
puzzle1_goal = create_object(exits.Exit, key="north", aliases =["n"], 
                                location =puzzle1, destination = goal)

hint_one = create_object(artifacts.HintShrine, key = "Large Statue", location = puzzle1)
clue_one = create_object(artifacts.ClueObject, key = "Mysterious Mural", location = puzzle1)
input_one = create_object(artifacts.AnswerObject, key = "Input Panel", location = puzzle1)

goal.db.desc = """
After solving all the puzzles, the players have reached the goal.
Players may complete the game here, but the door back south remains open.
"""
puzzle_entrance = create_object(exits.Exit, key="south", aliases =["s"], 
                                location =goal, destination = puzzle1)

limbo = search_object('Limbo')[0]
limbo_exit = create_object(exits.Exit, key = "enter world", aliases =["enter"],
                            location = limbo, destination = entrance)