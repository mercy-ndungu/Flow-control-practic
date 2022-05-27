from curses import ALL_MOUSE_EVENTS
from unittest import addModuleCleanup


class Bank:
    def __init__(self, accnumber, accname, bankname, balance):
        self.accnumber = accnumber
        self.accname = accname
        self.bankname = bankname
        self.balance = balance
        # Add these methods to class Account - deposit, withdraw. 
        # Create two instances of account and verify they work as expected.
    def withdraw(self):
        amount = int(input('Enter withdrawal amount:  '))
        self.balance-=amount
        return f"Your balance is {self.balance}"
    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        self.balance+=amount
        return f"Your new balance is {self.balance}"