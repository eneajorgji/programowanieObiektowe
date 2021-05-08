from abc import ABC, abstractmethod


# Dziedziczenie

class Ryba(ABC):
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga

    @abstractmethod
    def print(self):
        pass

    #    if self.wiek == 1:
    #        print(f"Ta ryba to {self.nazwa} ma {self.wiek} rok oraz waży {self.waga} kg")
    #        return None
    #    print(f"Ta ryba to {self.nazwa} ma {self.wiek} lat oraz waży {self.waga} kg")
    def urodziny(self):
        self.wiek += 1


class Slodkowodna(Ryba):
    def print(self):
        if self.wiek == 1:
            print(f"Ta słodkowodna ryba to {self.nazwa} ma {self.wiek} rok oraz waży {self.waga} kg")
            return None
        print(f"Ta słodkowodna ryba to {self.nazwa} ma {self.wiek} lat oraz waży {self.waga} kg")


class Slonowodna(Ryba):
    def __init__(self, nazwa, wiek, waga, morze):
        super().__init__(nazwa, wiek, waga)
        self.morze = morze

    def print(self):
        if self.wiek == 1:
            print(
                f"Ta słonowodna ryba to {self.nazwa} ma {self.wiek} rok oraz waży {self.waga} kg. Obszar występowania to {self.morze}")
            return None
        print(
            f"Ta słonowodna ryba to {self.nazwa} ma {self.wiek} lat oraz waży {self.waga} kg. Obszar występowania to {self.morze}")


class Test(Ryba):
    def print(self):
        print("Hello")


# ryba0 = Ryba("Jakaś tam", 5, 10.5)
ryba1 = Slodkowodna("Szczupak", 1, 0.8)
ryba2 = Slonowodna("Dorsz", 3, 2.1, "Bałtyk")
ryba2.urodziny()
# ryba0.print()
ryba1.print()
ryba2.print()
ob = Test("nazwa", 11, 12)
