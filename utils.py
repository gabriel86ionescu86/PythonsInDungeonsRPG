import os
import pygame
import random
import Enemy
import Player


# @staticmethod
def intro():
    print(
'''****************************************************************************************
* Welcome,stranger.                                                                    *
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons. *
* In a country where magic rules, anything is possible if you wish so.                 *
* It all depends on you, brave hero.                                                   *
****************************************************************************************
        ''')


# @staticmethod
def crossroads():
    os.system('clear')
    print(
"""You are in the middle of a crossroads.
You have 3 paths in front of you:
1. path going to a Village
2. path going to a Forest
3. path going to a Dessert""")
    path_option = input("Choose one with caution! --> ")
    os.system('clear')
    if path_option == '1':
        in_the_village()
    elif path_option == '2':
        in_the_forrest()
    elif path_option == '3':
        in_the_desert()
    return path_option


# @staticmethod
def player_type():
    player = ''
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
'''You have chosen to be a mighty wizard!
What is your name? --> ''')
        player = Player.Wizzard(player_name)
        os.system('clear')
        print(f"Intro to the world, {player_name}")
        input("Press enter to continue...")
        os.system('clear')
        print('Loading...')
    return player


# @staticmethod
def menu_music():
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound('Main_Menu2.mp3')
    pygame.mixer.stop()  # we stop the playing if there's another soundtrack running
    sound.play()


# @staticmethod
def explore_music():
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound('Exploring2.mp3')
    pygame.mixer.stop()  # we stop the playing if there's another soundtrack running
    sound.play()


# @staticmethod
def battle_music():
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound('Battle2.mp3')
    pygame.mixer.stop()  # we stop the playing if there's another soundtrack running
    sound.play()


# @staticmethod
def in_the_village():
    os.system('clear')
    print("You are in the village...")
    input("Press enter to continue")
    os.system('clear')


# @staticmethod
def in_the_forrest():
    os.system('clear')
    print("You are in the forrest...")
    input("Press enter to continue")
    os.system('clear')


# @staticmethod
def in_the_desert():
    os.system('clear')
    print("You are in the desert...")
    input("Press enter to continue")
    os.system('clear')


# @staticmethod
def battle_intro():
    enemy = ''
    battle_music()  # we import the explore_music function from utils.py
    print('From the underground an enemy appears!')
    random_number = random.randint(0, 2)
    if random_number == 0:
        enemy = Enemy.Goblin()
    elif random_number == 1:
        enemy = Enemy.Orc()
    elif random_number == 2:
        enemy = Enemy.Rat()
    print()
    input('Press enter to continue...')
    os.system('clear')
    return enemy


# @staticmethod
def battle_begins():
    print("First round of attack")
    random_number = random.randint(0, 1)
    if random_number == 0:
        print("You will attack first!")
        input('Press enter to continue')
        os.system('clear')
        player_attacks()
    else:
        print("The enemy attacks first! ")
        input('Press enter to continue')
        os.system('clear')
        enemy_attacks()
    return

def player_attacks():
    myself = player_type()
    him = battle_intro()
    print(f"Eu health ->> {myself.health}")
    print(f"Eu damage ->> {myself.damage}")
    print(f"Inamicul health ->> {him.health}")
    print(f"Inamicul damage ->> {him.damage}")
    while myself.health != 0 or him.health != 0:
        him.health -= myself.damage
        myself.health -= him.damage
    if myself.health == 0:
        print("You were defeated. Game over!")
        exit()
    else:
        print("You have won the battle!")
    return


def enemy_attacks():
    myself = player_type()
    him = battle_intro()
    print(f"Eu health ->> {myself.health}")
    print(f"Eu damage ->> {myself.damage}")
    print(f"Inamicul health ->> {him.health}")
    print(f"Inamicul damage ->> {him.damage}")
    while myself.health != 0 or him.health != 0:
        myself.health -= him.damage
        him.health -= myself.damage
    if myself.health == 0:
        print("You were defeated. Game over!")
        exit()
    else:
        print("You have won the battle!")
    return