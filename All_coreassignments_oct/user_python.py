class User:
    def __init__(self,first_name,email,amount,balance):
        self.first_name = first_name
        self.email = email
        self.amount = amount
        self.balance = balance
        # self.account = Bankaccount(int_rate=0.2, balance=0)


    def display_info(self):
        print(self.first_name)
        print("====================================")
        return self

   