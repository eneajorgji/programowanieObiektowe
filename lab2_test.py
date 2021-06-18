import math
from abc import ABC, abstractmethod


class GameObject():
    def __init__(self, health_point_count):
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
    def __init__(self, health_point_count):
        super().__init__(health_point_count)

    def interact(self):
        """
        musi wyswietlac informacje o tym ze gracz przeszedł przez drzwi
        """
        pass


class Monster(GameObject):
    def __init__(self, health_point_count):
        super().__init__(health_point_count)

    def interact(self):
        """
        musi zmniejszyc liczbe punktów zdrowie obiektu podanego jako argument
        (czyli gracza) o 10, nastepnie ustawic punkty zdrowia tego potwora na 0 i
        wyswietlic informacje o tym ze potwór
        został zabity przez gracza.
        """
        pass


class Door(GameObject):
    def __init__(self, health_point_count):
        super().__init__(health_point_count)

    def interact(self):
        """
        musi wyswietlac informacje o tym ze gracz przeszedł przez drzwi
        """
        pass


gracz = GameObject(100)
print(gracz.is_living())



