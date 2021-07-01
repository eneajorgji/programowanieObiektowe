#### Class 1 ####

class Account:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def credit(self, deposit):
        self.balance += deposit

    def debit(self, withdraw):
        self.balance -= withdraw

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def set_new_name(self, name):
        self.name = name


acc_1 = Account(200, "Adam Nowy")
print(acc_1.get_name())
print(acc_1.set_new_name("Adam Nowakowski"))
print(acc_1.get_name())
