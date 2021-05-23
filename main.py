import matplotlib.pyplot as plt
import datetime


class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def nalezy_do(self, other):
        if self.x * other.a + other.b == self.y:
            return True
        else:
            return False


class Prosta:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def miejsce_zerowe(self):
        try:
            miejsce_x = -self.b / self.a
            return miejsce_x, print(miejsce_x)
        except ZeroDivisionError:
            print("Brak miejsca zerowego,")


p = Punkt(1, 5)
pr = Prosta(2, 3)

print(p.nalezy_do(pr))
pr.miejsce_zerowe()


class Prostokat:
    def __init__(self, p1, p2):
        self.x = abs(p1.x - p2.x)
        self.y = abs(p1.y - p2.y)

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def rysuj(self, p1, p2):
        plt.plot([p1.x, p1.x], [p1.y, p2.y], c="blue")
        plt.plot([p2.x, p2.x], [p1.y, p2.y], c="blue")
        plt.plot([p1.x, p2.x], [p2.y, p2.y], c="blue")
        plt.plot([p1.x, p2.x], [p1.y, p1.y], c="blue")

        plt.scatter(p1.x, p1.y, c="red")
        plt.scatter(p2.x, p2.y, c="red")

        plt.grid()
        plt.show()
