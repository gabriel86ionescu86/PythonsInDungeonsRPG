#Create an rpg game that give messages along the way
import os
introMsg = '''
****************************************************************************************
* Welcome,stranger.                                                                    *
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons. *
* In a country where magic rules, anything is possible if you wish so.                 *
* It all depends on you, brave hero.                                                   *
****************************************************************************************
'''
print(introMsg)
print("Would you like to start the game? Y/N")
choice = input("Yes or No? -> ")
if choice.upper() == "Y" or choice.lower() == "y":
    print("OK")
    os.system('clear')
else:
    print("Thank you, good bye!")


