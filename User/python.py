# On instantiation of a user, the following attributes should be passed in as argument

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0


    def display_info (self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        print("================================")
        return self

    def enroll (self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self


    def spend_points(self,amount):
        self.gold_card_points = self.gold_card_points - amount 
        if self.is_rewards_member:
            print("user already a member.")
            return self
        return self



my_user = User("Javaris", "flick", "jpanther@yahoo.com", 24)
my_user.display_info().enroll().display_info().spend_points(100).display_info()

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = True
        self.gold_card_points = 1

    user_1 = User
    savingsaccount = User 
    user_2 = User
    bankaccount = User 

# first_name
# last_name
# email
# age
# Also include default attributes:

# is_rewards_member - default value of False
# gold_card_points = 0
# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.