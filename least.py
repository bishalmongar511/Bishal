class User_Account():
    def __init__(self, account_number, password, bank_type, balance_amount):
        self.account_number = account_number
        self.password = password
        self.bank_type = bank_type
        self.balance_amount = 0


    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Account balance has been updated: Nu{self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficient balance: Nu{self,balance}")
        else:
             self.balance = self.balance - amount
             print(f"Account balance has been updated: Nu{self.balance}")

    def check_balance(self):
        print(f"Current Balance: Nu {self.balance}")
        return self.balance
   
    def show_details(self):
        return f"{self.account_number},{self.password},{self.account_type},{self.balance}"

class Business_Account(User_Account):
     def __init__(self, account_number, password, bank_type, balance_amount):
        super(). __init__ (account_number, password, 'Business', balance_amount)

class Personal_Account(User_Account):
    def __init__(self, account_number, password, bank_type, balance_amount):
        super(). __init__ (account_number, password, 'Personal', balance_amount)


