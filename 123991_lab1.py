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

###########
# Zadanie 3
class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show_fraction(self):
        try:
            # return f"{self.a} / {self.b} jest {self.a / self.b}"
            if self.a > self.b:
                return f"{self.a // self.b} {self.a % self.b} / {self.b} "
            else:
                return f"{self.a} / {self.b}"
        except ZeroDivisionError:
            print(f"Mianownik jest {self.b}")

    @property
    def a(self):
        return self.a

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
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass


a, b = 5, 1
c, d = 1, 4
f1 = Fraction(a, b)
f2 = Fraction(c, d)
print(f1.show_fraction())
a = 4
print(f1.a())
f3 = f1 + f2
print(f3)
