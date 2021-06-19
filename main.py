#Create an rpg game that give messages along the way
import os
import Player
import Enemy

from utils import Mesaje as m
m.intro() # we import the intro function from utils.py
from utils import Music as ms
ms.menu_music() # we play the main menu music

print("Would you like to start the adventure? Y/N")
user_answer = input("Yes or No? -> ")
if user_answer.upper() == "Y" or user_answer.lower() == "y":
    print("OK")
    os.system('clear')
    from utils import Mesaje as ms
    ms.playerType() # we get the player type
else:
    print("Closing the program. Bye!")
    exit()

from utils import Music as ms
ms.explore_music() # we play the exploring music
from utils import Mesaje as m
m.crossroads() # we go to the crossroads
from utils import Battle as b
b.battle_intro() # we start a battle
b.battle_begins()