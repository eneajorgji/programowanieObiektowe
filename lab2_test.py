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


# Zadanie 3
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
