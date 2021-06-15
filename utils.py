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
        return


class Music:
    @staticmethod
    def menu_music():
        import pygame
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound('Main_Menu2.mp3')
        pygame.mixer.pause() # we stop the playing if there's another soundtrack running
        sound.play()

    @staticmethod
    def explore_music():
        import pygame
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound('Exploring2.mp3')
        pygame.mixer.pause() # we stop the playing if there's another soundtrack running
        sound.play()


    @staticmethod
    def battle_music():
        import pygame
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound('Battle2.mp3')
        pygame.mixer.pause() # we stop the playing if there's another soundtrack running
        sound.play()



