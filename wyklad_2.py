class Auto:
    licznik = 0

    def __init__(self, silnik, rok, marka):  # self odnosi sie do obiektu
        self.silnik = silnik
        self.rok = rok
        self.marka = marka
        self.public, self._protected, self.__private = 8, 10, 20
        Auto.licznik += 1

    def __del__(self):
        Auto.licznik -= 1

    def print(self):
        print(f"Auto ma {self.silnik}, zostal wyprodukoway w {self.rok} jest marki {self.marka}")

    @staticmethod
    def ile_auto():
        return Auto.licznik


car_1 = Auto(1.5, 2011, "Toyota")
car_2 = Auto(2.0, 1997, "Audi")
car_3 = Auto(1.1, 2016, "Fiat")

# Mozna teraz dodac metody
car_1.print()
car_2.print()
car_3.print()

print(car_1.marka)
print(car_1.public)
print(car_1._protected)
print(car_1._Auto__private)
car_3 = None
print(f"Liczba aut jest: {Auto.ile_auto()}")
