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
        # if self.a == 0:
        #     print("Brak miejsca zerowego,")
        # else:
        #     miejsce_x = -self.b / self.a
        #     return miejsce_x, print(miejsce_x)
        try:
            miejsce_x = -self.b / self.a
            return miejsce_x, print(miejsce_x)
        except ZeroDivisionError:
            print("Brak miejsca zerowego,")

p = Punkt(1, 5)
pr = Prosta(2, 3)

print(p.nalezy_do(pr))
pr.miejsce_zerowe()
