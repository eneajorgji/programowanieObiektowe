from abc import ABC, abstractclassmethod

# dziedziczenie
class Ryba:
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga
        self._pole = 1

    def print(self):
        if self.wiek == 1:
            print(f"Ta ryba to {self.nazwa} ma {self.wiek} rok oraz wazy {self.waga}")
            return None
        print(f"Ta ryba to {self.nazwa} ma {self.wiek} lat oraz wazy {self.waga}")

    def urodziny(self):
        self.wiek += 1


class Slodkowodna(Ryba):
    def print(self):
        if self.wiek == 1:
            print(f"Ta Slodkowodna ryba to {self.nazwa} ma {self.wiek} rok oraz wazy {self.waga}")
            return None
        print(f"Ta Slodkowodna ryba to {self.nazwa} ma {self.wiek} lat oraz wazy {self.waga}")


class Slonnowodna(Ryba):
    def __init__(self, nazwa, wiek, waga, morze):
        super().__init__(nazwa, wiek, waga)
        self.morze = morze

    def print(self):
        if self.wiek == 1:
            print(
                f"Ta Slonnowodna ryba to {self.nazwa} ma {self.wiek} rok oraz wazy {self.waga} kg, obszar wystepowania to {self.morze}.")
            return None
        print(f"Ta Slonnowodna ryba to {self.nazwa} ma {self.wiek} lat oraz wazy {self.waga} kg")


ryba_0 = Ryba("Pryzkladowa", 5, 10.5)

ryba_1 = Ryba("Okon", 3, 2.1)
ryba_2 = Slonnowodna("Szczupak", 1, .8, "Duze morze")
ryba_3 = Slodkowodna("Okon", 3, 2.1)

ryba_1.print()
ryba_2.print()
ryba_3.print()

print(ryba_0._pole)
