#### Class 1 ####
from scitools import *


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


#### Class 3 ####
class Vec2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq__


vec_1 = Vec2D(2.5, 3)
vec_2 = Vec2D(10, 10)
res = vec_1 + vec_2
print(vec_1.__add__(vec_2))
print(vec_1.__str__())
print(res)


##############
