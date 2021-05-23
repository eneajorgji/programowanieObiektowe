class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show_fraction(self):
        try:
            # return f"{self.a} / {self.b} jest {self.a / self.b}"
            if self.a > self.b:
                return f"{self.a // self.b} {self.a % self.b} / {self.b}"
            else:
                return f"{self.a} / {self.b}"
        except ZeroDivisionError:
            print(f"Mianownik jest {self.b}")

    # @property
    # def a(self):
    #     return self.a

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
# print(f1.a())
f3 = f1 + f2
print(f3)
