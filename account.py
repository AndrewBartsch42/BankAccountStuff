class account:
    #Contructor
    def __init__(self):
        self.name = "acount"
        self.balance = 0
        self.password = "password"
    def assign(self, account_name, account_balance, account_password):
        self.name = account_name
        self.balance = float(account_balance)
        self.password = account_password

    #checks the password
    def check_password(self, paswd):
        if paswd == self.password:
            return True
        else:
            print("incorrect password")
            return False

    #adds money to the balance of the account
    def deposit(self):
        amount = float(input("How much would you like to deposit?"))
        self.balance = self.balance + amount
        print("This is your new balance: ", self.balance)
        return None
    
    #removes money from the account and checks if it overdraws
    def withdraw(self):
        amount = float(input("How much would you like to withdraw?"))
        if amount > self.balance:
            print("you don't have that much money :(")
            return None
        else:
            self.balance = self.balance - amount
        print("This is your new balance: ", self.balance)
        return None
    
    #calls the deposit or withdraw functions depending on user input
    def change_balance(self):
        if self.check_password(input("What is your password? ")) == True:
            depositCheck = input("Would you like to deposit or withdraw (1 for deposit, 2 for withdraw)")
            if depositCheck == "1" or "2":
                if depositCheck == "1":
                    self.deposit()
                if depositCheck == "2":
                    self.withdraw()
            else:
                print("Invalid input please input a 1 for deposit or a 2 for withdraw. Please start again")
                return None
    #shows the balance
    def show_balance(self):
        print(self.balance)
    
    #only for debugging       
    def show(self):
       
        print(self.name)
        print(self.balance)
        print(self.password)
