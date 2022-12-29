    # class User:
    # def example_method(self):
    #     self.account.deposit(100)		# we can call the BankAccount instance's methods
    # 	print(self.account.balance)		# or access its attributes
# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
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
        print(self.balance)
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account = BankAccount(amount)
        print(self.account.amount)
        

user1 = User("name", "email")
user1.account.display_account_info()
# Update the User class __init__ method

# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
# Add a display_user_balance method to the User class that displays user's account balance

# SENSEI BONUS: Allow a user to have multiple accounts; 
# update methods so the user has to specify which account they are withdrawing or depositing to
# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance,
#  and transfers money from the user's account into another user's account.
class newcustomer:
    def __init__(self, name, email):
        self.name = name 
        self.email = email

    def transfer_money(self,amount, other_user):
        pass
        