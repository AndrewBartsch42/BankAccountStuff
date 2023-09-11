from account import account

class savings_account(account):
    # constructor
    def __init__(self, account_name, account_balance, account_password, id):
        self.id = id
        self.name = account_name
        self.balance = float(account_balance)
        self.password = account_password
        self.account_type = "savings"
        self.withdraw_limit = 1000.0
    #withdraw function for the savings account
    def withdraw(self):
        amount = float(input("How much would you like to withdraw?"))
        if amount > self.balance:
            print("you don't have that much money :(")
            return None
        if amount > self.withdraw_limit:
            print("Sorry that amount is not allowed")
            return None 
        else:
            self.balance = self.balance - amount
            print("This is your new balance: ", self.balance)
            return None
    def interest(self):
        self.balance = self.balance + (self.balance * 0.0043)
    
    def show_balance(self):
        self.interest()
        print(self.balance)