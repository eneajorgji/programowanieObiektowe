class Auta:
    rok_produkcji = 2021
    pojemnosc_silnika = 1000
    przebieg = 0
    kolor = "niebieski"

    def __init__(self, rp, ps, p, k):
        self.rok_produkcji = rp
        self.pojemnosc_silnika = ps
        self.przebieg = p
        self.kolor = k

    def print_rok(self):
        print(self.rok_produkcji)


obj = Auta(2016, 1600, 120000, "czarny")
obj.print_rok()


# co to jest obiekt i jak go uzywac
class Zespolona:
    def __init__(self, czesc_rzeczywista, czesc_urojona):
        self.a = czesc_rzeczywista
        self.b = czesc_urojona
        self.__dlugosc = self.length()  # pole prywatne, mamy dostęp tylko wewnotrz klasy

    def __str__(self):
        if self.b > 0:
            return str(self.a) + "+" + str(self.b) + "t"
        if self.b < 0:
            return str(self.a) + "-" + str(-self.b) + "t"

    def __add__(self, drugi_obiekt):
        return Zespolona(self.a + drugi_obiekt.a, self.b + drugi_obiekt.b)

    def length(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def length_2(self):
        return self.__dlugosc  # enkapsulacji: zamykamy dostep niektorych elementow


x = Zespolona(2, 3)
y = Zespolona(1, -4)
print(x)
print(y)
z = x + y
print(z)
print(z.length())
# print(z.dlugosc)
print(z.length_2())
