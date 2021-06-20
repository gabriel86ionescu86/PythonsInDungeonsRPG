import sys
import time
from random import randrange


class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self):
        pass


class Goblin(Enemy):
    def __init__(self):
        super(Goblin, self).__init__(99, 5)
        words = 'Glglg!!! I am a Goblin and I will slash you!!!'
        delay(words)


class Orc(Enemy):
    def __init__(self):
        super(Orc, self).__init__(98, 15)
        words = 'Wrarr, I am an Orc and I will cut you down!'
        delay(words)


class Rat(Enemy):
    def __init__(self):
        super(Rat, self).__init__(97, 10)
        words = 'Squil, I am a Rat and I will eat you up!'
        delay(words)


# @staticmethod
def delay(words):
    for i in words.split():
        sys.stdout.write("{} ".format(i))
        sys.stdout.flush()
        seconds = ".15" + str(randrange(1, 5, 2))
        seconds = float(seconds)
        time.sleep(seconds)
