from abc import ABC, abstractmethod
from random import random


class GameObject(ABC):
    def __init__(self, zycie=50):
        self.zycie = zycie

    def czy_zyje(self):
        if self.zycie > 0:
            return True
        else:
            return False

    @abstractmethod
    def interact(self):
        pass


class Player(GameObject):

    def interact(self):
        pass


class Door(GameObject):

    def interact(self, ob):
        print('Gracz przeszedł przez drzwi.')


class Monster(GameObject):

    def interact(self, ob):
        self.zycie = 0
        ob.zycie -= 10
        print('Gracz zabił potwora.')


player_1 = Player()
game = []

for i in range(10):
    if random() <= 0.7:
        action = Monster()
    else:
        action = Door()

    game.append(action)

for stage in game:
    if player_1.czy_zyje():
        stage.interact(player_1)
    else:
        print('Gracz został zabity!')
        break
