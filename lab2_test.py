import math
from abc import ABC, abstractmethod
from random import random


class GameObject(ABC):
    def __init__(self, health_point_count=50):
        self.health_point_count = health_point_count

    def is_living(self):
        if self.health_point_count > 0:
            return True
        else:
            return False

    @abstractmethod
    def interact(self):
        pass


class Player(GameObject):
    # def __init__(self, health_point_count):
    #     super().__init__(health_point_count)

    def interact(self):
        pass


class Door(GameObject):
    # def __init__(self, health_point_count):
    #     super().__init__(health_point_count)

    def interact(self, Player):
        """
        musi wyswietlac informacje o tym ze gracz przeszedł przez drzwi
        """
        print("Gracz przeszedl przez drzwi")


class Monster(GameObject):
    # def __init__(self, health_point_count):
    #     super().__init__(health_point_count)

    def interact(self, Player):
        """
        musi zmniejszyc liczbe punktów zdrowie obiektu podanego jako argument
        (czyli gracza) o 10, nastepnie ustawic punkty zdrowia tego potwora na 0 i
        wyswietlic informacje o tym ze potwór
        został zabity przez gracza.
        """
        self.health_point_count = 0
        Player.health_point_count -= 10
        print("Gracz zabil potwora")


player_first = Player()
game = []

for i in range(10):
    if random() <= .7:
        actions = Monster()
    else:
        actions = Door()
    game.append(actions)

for stage in game:
    if player_first.is_living():
        stage.interact(player_first)
    else:
        print("Gracz zostal zabity!")
        break
