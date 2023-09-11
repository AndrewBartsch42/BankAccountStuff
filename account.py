class account:
    #Contructor
    #def __init__(self):
        #initial_id = 0
        #self.name = "acount"
        #self.balance = 0
        #self.password = "password"
        #self.id = initial_id
        #initial_id = initial_id + 1


    def __init__(self, account_name, account_balance, account_password):
        self.name = account_name
        self.balance = float(account_balance)
        self.password = account_password

    #checks the password
    def check_password(self, paswd, accounts):
        i = 0
        while (i < len(accounts)):
            if accounts[i].password == paswd:
                #print("breaking")
                break         
            i = i + 1
        if paswd == accounts[i].password:
            return True
        else:
            print("incorrect password")
            return False
    #finds the account in the accounts array by using the password
    def find_id(accounts):
        id = int(input("What is your id?"))
        i = 0
        while (i < len(accounts) - 1):
            if accounts[i].id == id:
                #print("breaking")
                break
            i = i + 1
        return i
    #adds money to the balance of the account
    def deposit(self, id, accounts):
        amount = float(input("How much would you like to deposit?"))
        accounts[id].balance = accounts[id].balance + amount
        print("This is your new balance: ", accounts[id].balance)
        return None
    
    #removes money from the account and checks if it overdraws
    def withdraw(self):
        amount = float(input("How much would you like to withdraw?"))
        if amount > self.balance:
            print("you don't have that much money :[")
            return None
        else:
            self.balance = self.balance - amount
        print("This is your new balance: ", self.balance)
        return None
    
    #calls the deposit or withdraw functions depending on user input
    def change_balance(self, accounts):
        passwd = input("What is your password? ")
        if account.check_password(self, passwd, accounts) == True:
            i = 0
            while (i < len(accounts)):
                if accounts[i].password == passwd:
                    break
                else:
                    i = i + 1
            depositCheck = input("Would you like to deposit or withdraw 1 for deposit, 2 for withdraw")
            if depositCheck == "1" or "2":
                if depositCheck == "1":
                    account.deposit(self, account.find_id(accounts), accounts)
                if depositCheck == "2":
                    account.withdraw(accounts[i])
            else:
                print("Invalid input please input a 1 for deposit or a 2 for withdraw. Please start again")
                return None
    #shows the balance
    def show_balance(self, accounts):
        id =int(account.find_id(accounts))
        print(id)
        passwd = input("What is your password?")
        account.check_password(self, passwd, accounts)
        print(accounts[id].balance)

    
    #used to show id and other stuff    
    def show(self, accounts):
        print("This is your id please keep it on you as it will be used to id you later")
        print(accounts[len(accounts) - 1].id)
