import os
import pygame
import random
import Enemy
import Player

class Mesaje:
    @staticmethod
    def intro():
        print(
'''****************************************************************************************
* Welcome,stranger.                                                                    *
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons. *
* In a country where magic rules, anything is possible if you wish so.                 *
* It all depends on you, brave hero.                                                   *
****************************************************************************************
        ''')


    @staticmethod
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
        if (path_option) == '1':
            Paths.in_the_village()
        elif (path_option) == '2':
            Paths.in_the_forrest()
        elif (path_option) == '3':
            Paths.in_the_desert()
        return path_option


    @staticmethod
    def playerType():
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
'''You have chosen to be a mighty wizzard!
What is your name? --> ''')
            player = Player.Wizzard(player_name)
            os.system('clear')
            print(f"Intro to the world, {player_name}")
            input("Press enter to continue...")
            os.system('clear')
            print('Loading...')
        return player


class Music:
    @staticmethod
    def menu_music():
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound('Main_Menu2.mp3')
        pygame.mixer.stop() # we stop the playing if there's another soundtrack running
        sound.play()


    @staticmethod
    def explore_music():
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound('Exploring2.mp3')
        pygame.mixer.stop() # we stop the playing if there's another soundtrack running
        sound.play()


    @staticmethod
    def battle_music():
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound('Battle2.mp3')
        pygame.mixer.stop() # we stop the playing if there's another soundtrack running
        sound.play()


class Paths:
    @staticmethod
    def in_the_village():
        os.system('clear')
        print("You are in the village...")
        input("Press enter to continue")
        os.system('clear')


    @staticmethod
    def in_the_forrest():
        os.system('clear')
        print("You are in the forrest...")
        input("Press enter to continue")
        os.system('clear')


    @staticmethod
    def in_the_desert():
        os.system('clear')
        print("You are in the desert...")
        input("Press enter to continue")
        os.system('clear')


class Battle:
    @staticmethod
    def battle_intro():
        Music.battle_music()  # we import the explore_music function from utils.py
        print('From the underground an enemy appears!')
        random_number = random.randint(0, 2)
        if random_number == 0:
            enemy = Enemy.Goblin()
        elif random_number == 1:
            enemy = Enemy.Orc()
        elif random_number == 2:
            enemy = Enemy.Rat()
        input('Press enter to continue...')
        os.system('clear')


    @staticmethod
    def battle_begins():
        print("First round of attack")
        random_number = random.randint(0, 1)
        if random_number == 0:
            print("You will attack first!")
            input('Press enter to continue')
            os.system('clear')
            # wip, neeed to call the Battle.player_attacks()
        else:
            print("The enemy attacks first! ")
            input('Press enter to continue')
            os.system('clear')
            # wip, neeed to call the Battle.enemy_attacks()
            pass


    # @staticmethod
    # def player_attacks:
    #     while player.health != 0 or enemy.health != 0:
    #         Enemy.Enemy(health) -= Player.Player(health)
    #         Player.Player(health) -= Enemy.Enemy(damage)
    #     if Player.Player(health) == 0:
    #         print("You were defeated. Game over!")
    #         exit()
    #     else:
    #         print("You have won the battle!")


    # @staticmethod
    # def enemy_attacks:
    #     while player.health != 0 or enemy.health != 0:
    #         Player.Player(health) -= Enemy.Enemy(damage)
    #         Enemy.Enemy(health) -= Player.Player(health)
    #     if Player.Player(health) == 0:
    #         print("You were defeated. Game over!")
    #         exit()
    #     else:
    #         print("You have won the battle!")
