from evennia import create_object, search_object
from typeclasses import rooms, exits, artifacts

entrance = create_object(rooms.Room, key ="entrance")
puzzle1 = create_object(rooms.Room, key = "puzzle1")
goal = create_object(rooms.Room, key = "exit")

entrance.db.desc = """
The year is 1524, you and your companions are conquistadores operating for the Spanish Empire in the Americas. Part
of a force led by Pedro de Alvarado, your team has stumbled upon a pristine untouched temple. Seeing the possibility of
getting the first pick of valuable treasure for yourselves, you and your friends decide to immediately climb the stairs
and enter the temple.

Upon entering, the door slams shut behind you, and you find yourself in a room with strangely glowing artifacts.
"""

entrance_puzzle1 = create_object(exits.Exit, key="north", aliases =["n"], 
                                location =entrance, destination = puzzle1)

red_arti = create_object(artifacts.Red, key = "Red Artifact", location = entrance)
blue_arti = create_object(artifacts.Blue, key = "Blue Artifact", location = entrance)
green_arti = create_object(artifacts.Green, key = "Green Artifact", location = entrance)
yellow_arti = create_object(artifacts.Yellow, key = "Yellow Artifact", location = entrance)

puzzle1.db.desc = """
You find yourself in another chamber with strange statues and murals.
There seems to be a closed door with some sort of panel next to it.
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