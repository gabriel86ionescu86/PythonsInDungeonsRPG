class Mesaje:
    @staticmethod
    def intro():
        import os
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
        import os
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
            from utils import Paths as p
            p.in_the_village()
        elif (path_option) == '2':
            from utils import Paths as p
            p.in_the_forrest()
        elif (path_option) == '3':
            from utils import Paths as p
            p.in_the_dessert()
        return


class Music:
    @staticmethod
    def menu_music():
        import pygame
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound('Main_Menu2.mp3')
        pygame.mixer.stop() # we stop the playing if there's another soundtrack running
        sound.play()


    @staticmethod
    def explore_music():
        import pygame
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound('Exploring2.mp3')
        pygame.mixer.stop() # we stop the playing if there's another soundtrack running
        sound.play()


    @staticmethod
    def battle_music():
        import pygame
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound('Battle2.mp3')
        pygame.mixer.stop() # we stop the playing if there's another soundtrack running
        sound.play()


'''create a method path(userPath)
 that uses the returned value from crossroads method'''


class Paths:
    @staticmethod
    def in_the_village():
        import os
        import random
        import Enemy
        os.system('clear')
        print("You are in the village...")
        input("Press enter to continue")
        os.system('clear')
        print('From a backside alley an enemy appears!')
        from utils import Music as ms
        ms.battle_music()  # we import the explore_music function from utils.py
        random_number = random.randint(0,2)
        if random_number == 0:
            enemy = Enemy.Goblin()
        elif random_number == 1:
            enemy = Enemy.Orc()
        elif random_number == 2:
            enemy = Enemy.Rat()
        input("Press enter to continue")
        os.system('clear')

    @staticmethod
    def in_the_forrest():
        pass

    @staticmethod
    def in_the_desert():
        pass