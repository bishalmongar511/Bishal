import random
import string

# Base Account class
class Account:
    def __init__(self, account_number, password, account_type, balance=0):
        self.account_number = account_number
        self.password = password
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, 'Personal', balance)

class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, 'Business', balance)

def generate_account_number():
    return ''.join(random.choices(string.digits, k=10))

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
