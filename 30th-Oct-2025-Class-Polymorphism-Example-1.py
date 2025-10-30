# ---------------------------------------------------------------
# Class-Assignment: Demonstrate Polymorphism in Python using Bank Account classes
# Name: Sheikh Saqib
# Date: 30th-Oct-2025
# ---------------------------------------------------------------
# Explanation:
# Polymorphism means "many forms" — in OOP, it allows the same method name
# to perform different actions depending on the object calling it.
#
# In this example, we create a base class `BankAccount` and two derived classes:
# `SavingsAccount` and `CurrentAccount`. Both override the `withdraw()` method
# to show different withdrawal rules.
#
# We use obj.__class__.__name__ in print statements to display each class name
# dynamically — this helps show polymorphism in action.
# ---------------------------------------------------------------

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.__class__.__name__}: Deposited {amount}. New balance = {self.balance}")

    def withdraw(self, amount):
        """Base withdraw method (to be overridden by subclasses)"""
        print(f"{self.__class__.__name__}: Generic withdrawal — override in subclass")

    def display_balance(self):
        print(f"{self.__class__.__name__}: {self.name}'s current balance = {self.balance}")


# ---------------------------------------------------------------
# Subclass 1 – Savings Account
# ---------------------------------------------------------------
class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.__class__.__name__}: Insufficient balance! Cannot withdraw {amount}.")
        else:
            self.balance -= amount
            print(f"{self.__class__.__name__}: Withdrawn {amount}. Remaining balance = {self.balance}")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"{self.__class__.__name__}: Interest added = {interest}. New balance = {self.balance}")


# ---------------------------------------------------------------
# Subclass 2 – Current Account
# ---------------------------------------------------------------
class CurrentAccount(BankAccount):
    def __init__(self, name, balance, overdraft_limit=5000):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print(f"{self.__class__.__name__}: Overdraft limit exceeded! Cannot withdraw {amount}.")
        else:
            self.balance -= amount
            print(f"{self.__class__.__name__}: Withdrawn {amount}. Remaining balance = {self.balance}")

    def charge_fee(self, fee):
        self.balance -= fee
        print(f"{self.__class__.__name__}: Fee of {fee} charged. Remaining balance = {self.balance}")


# ---------------------------------------------------------------
# Demonstration of Polymorphism
# ---------------------------------------------------------------

# Create a list of different account types (same interface, different behavior)
accounts = [
    SavingsAccount("Alice", 1000),
    CurrentAccount("Bob", 2000),
    BankAccount("Charlie", 500)  # Base class instance
]

print("\n--- Performing Deposits ---")
for acc in accounts:
    acc.deposit(500)  # same method name, different output if overridden

print("\n--- Performing Withdrawals (Polymorphism in action) ---")
for acc in accounts:
    acc.withdraw(1200)  # all have withdraw(), but different behaviors

print("\n--- Displaying Balances ---")
for acc in accounts:
    acc.display_balance()

print("\n--- Adding Interest and Fees (Specific to Subclasses) ---")
# We can still call subclass-specific methods if needed
accounts[0].add_interest()  # only for SavingsAccount
accounts[1].charge_fee(200) # only for CurrentAccount
