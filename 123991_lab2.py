from abc import ABC, abstractmethod

# Zadanie 1
print("\n### Zadanie 1 ###\n")


class Ssak():
    def __init__(self, info, rodzaj):
        self.info = info
        self.rodzaj = rodzaj
        print("Stworzyles:", self.rodzaj)

    def ciekawostka(self):
        return f"Ciekawostwa o {self.rodzaj} jest: {self.info}"


class Ssak_1(Ssak):  # KOT
    def __init__(self, info, rodzaj):
        super().__init__(info, rodzaj)


class Ssak_2(Ssak):  # LEW
    def __init__(self, info, rodzaj):
        super().__init__(info, rodzaj)


s = Ssak("Brak ciekawosci", "Pies")
print(s.ciekawostka())

k = Ssak_1("ma 7 zyc", "kot")
print(k.ciekawostka())

l = Ssak_2("moze zyc w dziungli", "lew")
print(l.ciekawostka())

# Zadanie 2
print("\n### Zadanie 2 ###\n")


class GameObject(ABC):
    def __init__(self, health_point_count):
        self.health_point_count = health_point_count

    def is_living(self):
        if self.health_point_count > 0:
            return True
        else:
            return False

    @abstractmethod
    def interact(self):
        pass
