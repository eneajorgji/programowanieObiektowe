import math
from abc import ABC, abstractmethod

# Zadanie 1
from random import random

print("\n### Zadanie 1 ###\n")


class Ssak():
    def __init__(self, info, rodzaj):
        self.info = info
        self.rodzaj = rodzaj
        print("Stworzyles:", self.rodzaj)

    def ciekawostka(self):
        return f"Ciekawostwa o {self.rodzaj} jest: {self.info}"


class Ssak_1(Ssak):  # KOT
    def __init__(self, info, rodzaj):
        super().__init__(info, rodzaj)


class Ssak_2(Ssak):  # LEW
    def __init__(self, info, rodzaj):
        super().__init__(info, rodzaj)


s = Ssak("Brak ciekawosci", "Pies")
print(s.ciekawostka())

k = Ssak_1("ma 7 zyc", "kot")
print(k.ciekawostka())

l = Ssak_2("moze zyc w dziungli", "lew")
print(l.ciekawostka())

# Zadanie 2
print("\n### Zadanie 2 ###\n")

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



class GameObject(ABC):
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


# Zadanie 3
print("\n### Zadanie 3 ###\n")

class Equation(ABC):
    def __init__(self, a):
        self.a = a

    @abstractmethod
    def solve(self):
        if len(self.a) == 2:
            if self.a[0] == 0:
                if self.a[1] == 0:
                    print("Rownanie ma wiele rozwiazan")
                else:
                    print("Nie ma rozwiazan")
            else:
                x = - self.a[1] / self.a[0]
                print("x =", x)
        else:
            if self.a[0] == 0:
                print("Nie jest rownanie kwadratowe")
            else:
                delta = (self.a[1] * self.a[1]) - 4 * (self.a[0]) * (self.a[2])
                if delta > 0:
                    x1 = (-self.a[1] - math.sqrt(delta)) / (2 * self.a[0])
                    x2 = (-self.a[1] + math.sqrt(delta)) / (2 * self.a[0])
                    print("x1 =", x1)
                    print("x2 =", x2)
                elif delta == 0:
                    xx = (-self.a[1]) / (2 * self.a[0])
                    print("x =", xx)
                else:
                    print("Rownanie nie ma rozwiazan")


class LinearEquation(Equation):
    def __init__(self, a):
        super().__init__(a)

    def solve(self):
        super().solve()


class QuadraticEquation(Equation):
    def __init__(self, a):
        super().__init__(a)

    def solve(self):
        super().solve()


eq = LinearEquation([2, 0])
eq.solve()
print(30 * "#")

eq1 = LinearEquation([0, 2])
eq1.solve()
print(30 * "#")

eq2 = QuadraticEquation([1, 5, 6])
eq2.solve()
print(30 * "#")

