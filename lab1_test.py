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

