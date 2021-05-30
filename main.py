import datetime


###########
# Zadanie 3

class Note:
    czas_stworzenia = datetime.datetime.now()

    def __init__(self, autor, tresc):
        self.autor = autor
        self.tresc = tresc
        self.t = ""

    def get_time(self):
        t = datetime.datetime.now()
        return t

    def __repr__(self):
        return f"Notatka: ({self.autor}, {self.tresc})"


class Notebook:
    def __init__(self):
        self.list_of_notes = ["taki przykład fgkjd asdjkhf askjdf sdjkla"]

    def add_new(self):
        self.list_of_notes.append()
        pass

    def add_existing_note(self):
        pass

    def len(self):
        print("Jest", len(self.list_of_notes), "dodanych notatek.")

    def print_note(self):
        licznik = 0
        for i in self.list_of_notes:
            licznik += 1
            print(i)
        print(licznik)


# nb = Notebook()
# nb.add_new("Bartek", "Dokoncz instrukcje")


n = Note("a", "B")
print("Godzina to:", n.get_time())
