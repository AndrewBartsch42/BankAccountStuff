from account import account

class checking_account(account):
    #contructor
    def __init__(self, account_name, account_balance, account_password, id):
        self.id = id
        self.name = account_name
        self.balance = float(account_balance)
        self.password = account_password
        self.account_type = "checking"
    
    
