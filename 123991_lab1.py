import matplotlib.pyplot as plt
import datetime


###########
# Zadanie 1

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


###########
# Zadanie 2
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


p1 = Punkt(1, 1)
p2 = Punkt(2, 3)

prost = Prostokat(p1, p2)
print("Pole wynosi: ", prost.pole())

print("Obwod wynosi: ", prost.obwod())

prost.rysuj(p1, p2)


###########
# Zadanie 3
class Note:
    czas_stworzenia = datetime.datetime.now()

    def __init__(self, autor, tresc):
        self.autor = autor
        self.tresc = tresc

    def __repr__(self):
        return f"Notatka: ({self.autor}, {self.tresc})"


class Notebook(Note):
    def __init__(self):
        super(Notebook, self).__init__()
        self.lista = []
        pass

    def add_new(self):
        self.lista.append(self.tresc)
        pass


###########
# Zadanie 4
class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show_fraction(self):
        try:
            return f"{self.a} / {self.b}"
        except ZeroDivisionError:
            print(f"Mianownik jest {self.b}")

    def __repr__(self):
        return repr(self.a) + "/" + repr(self.b)

    def __str__(self):
        return str(self.a) + "/" + str(self.b)

    def __add__(self, other):
        if b != d:
            new_a = self.a * other.b + self.b * other.a
            new_b = self.b * other.b
        else:
            new_a = self.a + other.a
            new_b = self.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        return self.a * other.d - self.b * other.c

    def __mul__(self, other):
        return self.a * other.c, "/", self.b * other.d

    def div(self, other):
        return self.a * other.d, "/", self.b * other.c


a, b = 5, 2
c, d = 1, 4
f1 = Fraction(a, b)

print(f1)