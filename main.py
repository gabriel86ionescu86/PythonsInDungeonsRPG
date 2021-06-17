#Create an rpg game that give messages along the way
import os
import Player
import Enemy

from utils import Mesaje as m
m.intro() # we import the intro function from utils.py
from utils import Music as ms
ms.menu_music() # we import the menu_music function from utils.py

print("Would you like to start the adventure? Y/N")
user_answer = input("Yes or No? -> ")
if user_answer.upper() == "Y" or user_answer.lower() == "y":
    print("OK")
    os.system('clear')
    answer = input(
"""What type of player are you:
1 for Warrior
2 for Wizard
--> """)
    if answer == '1':
        os.system('clear')
        player_name = input(
'''You have chosen to be a mighty warrior!
What is your name? -> ''')
        player = Player.Warrior(player_name)
        os.system('clear')
        print(f"Intro to the world, {player_name}")
        input("Press enter to continue...")
        os.system('clear')
        print('Loading...')
    elif answer == '2':
        os.system('clear')
        player_name = input(
'''You have chosen to be a mighty wizzard!
What is your name? --> ''')
        player = Player.Wizzard(player_name)
        os.system('clear')
        print(f"Intro to the world, {player_name}")
        input("Press enter to continue...")
        os.system('clear')
        print('Loading...')
else:
    print("Closing the program. Bye!")
    exit()

from utils import Music as ms
ms.explore_music() # we import the explore_music function from utils.py
from utils import Mesaje as m
m.crossroads() # we import the crossroads function from utils.py

