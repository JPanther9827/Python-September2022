user1.display_info()
user1.enroll()
user1.spend_points(50)
user1.display_info()
user2.enroll()
user2.spend_points(80)
user2.display_info()

user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()

class User:
    # .. constructor
    
    def display_info(self):
        # your code
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




        
    	# new return statement, returns this same object
        return self


