# Create an rpg game that give messages along the way
import os
import utils

utils.intro()  # we import the intro function from utils.py
utils.menu_music()  # we play the main menu music
print("Would you like to start the adventure? Y/N")
user_answer = input("Yes or No? -> ")
if user_answer.upper() == "Y" or user_answer.lower() == "y":
    print("OK")
    os.system('clear')
    utils.player_type()  # we get the player type
else:
    print("Closing the program. Bye!")
    exit()
utils.explore_music()  # we play the exploring music
utils.crossroads()  # we go to the crossroads
utils.battle_intro()  # we start a battle
utils.battle_begins()
