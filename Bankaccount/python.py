# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount +=
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# -= print (Insufficient funds: Charging a $5 fee" and deduct $5)
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
# This means we need a class that looks something like this:
# Create a BankAccount class with the attributes interest rate and balance
# Add a deposit method to the BankAccount class
# Add a withdraw method to the BankAccount class
# Add a display_account_info method to the BankAccount class
# Add a yield_interest method to the BankAccount class


class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance 
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        # print(self.balance)
        return self

    def withdraw(self, amount):
        self.balance = self.balance - amount
        # print(self.balance)
        return self

    def display_account_info(self):
        print(f"display_account_info")
        return self

    def yield_interest(self):
        self.balance = self.balance
        return self

    # def yield_interest(self):
    #     yield_interest("")
account_type1 = BankAccount(.01,100)
account_type1.deposit(100)
account_type1.withdraw(50)
account_type1.display_account_info()
account_type1.yield_interest()
# invoking it

# Create 2 accounts:

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
BankAccount
account_type1.deposit(100).deposit(100).deposit(100).yield_interest().withdraw(50).display_account_info()
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

account_type1.deposit(200).deposit(200).withdraw(50).withdraw(20).withdraw(10).withdraw(10).yield_interest().display_account_info()
