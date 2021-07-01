#### Class 1 ####

class Account:
    def __init__(self, balance, name, account_number):
        self._balance = balance
        self._name = name
        self._account_number = account_number

    def credit(self, deposit):
        self._balance += deposit

    def debit(self, withdraw):
        self._balance -= withdraw

    def get_balance(self):
        return self._balance

    def get_name(self):
        return self._name

    def set_new_name(self, name):
        self._name = name

    def print_info(self):
        return f"This account belong to {self._name}, " \
               f"it contains {self._balance} PLN, " \
               f"of account number {self._account_number}"


acc_1 = Account(2000, "Adam Nowy", 1001_2001_3002)
print(acc_1.get_name())
print(acc_1.set_new_name("Adam Nowakowski"))
print(acc_1.get_name())
print(acc_1.print_info())


#### Class 2 ####

class PhoneBook:
    def __init__(self, name, phone_number, address=None, email=None):
        self.name = name
        self.phone_number = phone_number
        self._address = address
        self.email = email

    def set_new_name(self, name):
        self.name = name

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def add_address(self, address):
        self._address = address

    def print_phone_details(self):
        return f"Name: {self.name} \nPhone Number: {self.phone_number} \nAddress: {self._address}"


person_1 = PhoneBook("Adam Nowy", 333444111222, email="adamnowy@myemail.com")
print(person_1.print_phone_details())
