class Samochod:
    def __init__(self, nazwa, rocznik, pojemnosc, kolor, przebieg):
        self.nazwa = nazwa
        self.rocznik = rocznik
        self.pojemnosc = pojemnosc
        self.kolor = kolor
        self.przebieg = przebieg
        self.ciek = "Jest to auto osobowe"

    def print(self):
        print("KupiÅ‚em sobie auto", self.nazwa, "z rocznika", self.rocznik, "o pojemnosci", self.pojemnosc,
              "ktore jest koloru", self.kolor, ".", "Jego przebieg to", self.przebieg)

    def ciekawostka(self):
        print(self.ciek)

    def __sub__(self, rocznik):
        print("Roznica lat aut to")
        return sam2.rocznik - sam1.rocznik

    def __gt__(self, rocznik):
        print("Czy", sam1.nazwa, 'jest starszy od', sam2.nazwa, "?")
        return sam1.rocznik > sam2.rocznik


sam1 = Samochod('Renault', 1932, 800, 'czarny', 499999)
sam1.print()
sam2 = Samochod('Ford', 1992, 1598, 'bialy', 249000)
sam2.print()
sam2.ciekawostka()
print(sam2 - sam1)
print(sam1 > sam2)


class Student:
    def __init__(self, imie, nazwisko, wiek, rok, srednia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.rok = rok
        self.srednia = srednia
        self.ciek = "To sa studenci dzienni"

    def print(self):
        print("Student", self.imie, self.nazwisko, "ma", self.wiek, "jest na", self.rok, "roku.", "Jego srednia to",
              self.srednia)

    def ciekawostka(self):
        print(self.ciek)

    def __add__(self, srednia):
        print("Student 1 ma srednia", st1.srednia, "Student 2 ma srednia", st2.srednia, "Razem maja")
        return st1.srednia + st2.srednia

    def __gt__(self, wiek):
        print("Czy", st1.nazwisko, 'jest starszy od', st2.nazwisko, "?")
        return st2.wiek > st2.wiek


st1 = Student('Jan', 'Kowalski', 19, 'pierwszy', 4.2)
st1.print()
st2 = Student('Piotr', 'Nowak', 22, "drugi", 3.2)
st2.print()
st2.ciekawostka()
print(st1 + st2)
print(st1 > st2)


class Kot:
    def __init__(self, rasa, waga, wiek, siersc, pochodzenie):
        self.rasa = rasa
        self.waga = waga
        self.wiek = wiek
        self.siersc = siersc
        self.pochodzenie = pochodzenie
        self.ciek = "Sa rozne koty"

    def print(self):
        print("Kot", self.rasa, "wazy", self.waga, "ma", self.wiek, "lat.", "Ma", self.siersc, "siersc.", "Pochodzi z",
              self.pochodzenie)

    def ciekawostka(self):
        print(self.ciek)

    def __add__(self, waga):
        print("Kot perski wazy", kt1.waga, "Kot syjamski wazy", kt2.waga)
        return kt1.waga + kt2.waga

    def __gt__(self, wiek):
        print("Czy", kt1.wiek, 'jest starszy od', kt2.wiek, "?")
        return kt1.wiek > kt2.wiek


kt1 = Kot('Perski', 3, 4, 'duzo', 'Iran')
kt1.print()
kt2 = Kot('Sycylijski', 5, 5, "malo", 'Australia')
kt2.print()
kt2.ciekawostka()
print(kt1 + kt2)
print(kt1 > kt2)


class Czlowiek:
    def __init__(self, plec, waga, wiek, wzrost, narodowosc):
        self.plec = plec
        self.waga = waga
        self.wiek = wiek
        self.wzrost = wzrost
        self.narodowosc = narodowosc
        self.ciek = "Liczba ludnosci liczona jest w miliardach"

    def print(self):
        print("Dany czlowiek to", self.plec, "wazy", self.waga, "ma", self.wiek, "lat.", "Ma", self.wzrost,
              "cm wzrostu.", "Ten czlowiek to", self.narodowosc)

    def ciekawostka(self):
        print(self.ciek)

    def __add__(self, waga):
        print("Pierwszy czlowiek wazy", cz1.waga, "Drugi czlowiek wazy", cz2.waga, "Razem waza")
        return cz1.waga + cz2.waga

    def __gt__(self, wiek):
        print("Czy", cz1.wiek, 'jest mlodszy od', cz2.wiek, "?")
        return cz2.wiek < cz2.wiek


cz1 = Czlowiek('Mezczyzna', 89, 54, 180, 'Polak')
cz1.print()
cz2 = Czlowiek('Kobieta', 55, 32, 170, 'Australijczyk')
cz2.print()
cz2.ciekawostka()
print(cz1 + cz2)
print(cz2 < cz1)


class Film:
    def __init__(self, tytul, dlugosc, rokprod, krajprod, gatunek):
        self.tytul = tytul
        self.dlugosc = dlugosc
        self.rokprod = rokprod
        self.krajprod = krajprod
        self.gatunek = gatunek
        self.ciek = "Najdluzej trwaja filmy Bollywood"

    def print(self):
        print("Film", self.tytul, "trwa", self.dlugosc, "min.", "i zostal wyprodukowany w", self.rokprod, "roku.",
              self.gatunek, "wyprodukowano w ", self.krajprod)

    def ciekawostka(self):
        print(self.ciek)

    def __add__(self, dlugosc):
        print("Pierwszy film trwa", fm1.dlugosc, "Drugi film trwa", fm2.dlugosc, "Razem ogladanie zajmie dÅ‚ugo")
        return fm1.dlugosc + fm2.dlugosc

    def __gt__(self, rokprod):
        print("Czy", fm1.rokprod, 'jest starszy od', fm2.rokprod, "?")
        return fm1.rokprod > fm2.rokprod


fm1 = Film('Milosc', 89, 1954, "PL", 'Melodramat')
fm1.print()
fm2 = Film('Kids', 121, 1999, "USA", 'Komedia')
fm2.print()
fm2.ciekawostka()
print(fm1 + fm2)
print(fm1 > fm2)


class Student:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print("Mam na imie", self.imie, "Moje nazwisko to", self.nazwisko, "i mam", self.wiek)

    def urodziny(self):
        print("Urodzilem sie w", 2021 - self.wiek)


class Album1(Student):
    pass


class Album2(Student):
    pass


def main():
    Piotr = Album1("Piotr", "Jankowski", 44)
    Pawel = Album2("Pawel", "Rodz", 34)

    Piotr.przedstaw_sie()
    Piotr.urodziny()

    Pawel.przedstaw_sie()
    Pawel.urodziny()


if _name_ == "_main_":
    main()


class Rodzina:
    def __init__(self, imie, pokrewienstwo, wiek, info):
        self.imie = imie
        self.pokrewienstwo = pokrewienstwo
        self.wiek = wiek
        self.info = "Ta rodzinka jest dziwna"

    def przedstaw_sie(self):
        print("Mam na imie", self.imie, "W tej rodzinie jestem", self.pokrewienstwo, "i mam", self.wiek, "lat")

    def urodziny(self):
        print("Urodzilem sie w", 2021 - self.wiek)


class Rysiek(Rodzina):
    def __init__(self):
        super().__init__("Rysiek")


class Anna(Rodzina):
    def __init__(self):
        super().__init__("Anna")


def main():
    Syn = Rysiek("Rysiek", "Syn", 44)
    Corka = Anna("Anna", "Corka", 34)

    Syn.przedstaw_sie()
    Syn.urodziny()

    Corka.przedstaw_sie()
    Corka.urodziny()
