import datetime


###########
# Zadanie 3

class Note:

    def __init__(self, autor, tresc):
        self.autor = autor
        self.tresc = tresc

    def get_time(self):
        self.t = datetime.datetime.now()
        return self.t.strftime("%H:%M")

    # TODO
    def __repr__(self):
        return f"Notatka: ({self.autor}, {self.tresc})"


class Notebook():
    list_of_notes = []

    # def __init__(self):
    #     super().__init__()

    # TODO
    def add_new(self):
        return

    # TODO
    def add_existing_note(self):
        pass

    # TODO
    def len(self):
        print("Jest", len(self.list_of_notes), "dodanych notatek.")

    # TODO
    def print_note(self):
        count = 0
        for i in self.list_of_notes:
            count += 1
            print(i)
        print(count)


# nb = Notebook()
# nb.add_new("Bartek")

n = Note("a", "b")

print("Godzina to:", n.get_time())
