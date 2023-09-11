from account import account
from checking_account import checking_account
from savings_account import savings_account


class main:
    
    def __init__(self):
        self.running = True
  
    
    def menu(self, accounts):
        id = len(accounts)
        print("---------------------")
        print("1 for create account")
        print("2 for change balance")
        print("3 for show balance")
        print("4 for exit")
        print("---------------------")
        menu_input = int(input("\n"))
        if (menu_input == 1):
            account1_name = input("what is your name? ")
            account1_balance = float(input("What is your starting balance? "))
            account1_password = input("What is your password? ")
            account1_type = int(input("Checkings or savings (press 1 for checkings and 2 for savings)"))
            if (account1_type == 1):
                accounts.append(checking_account(account1_name, account1_balance, account1_password, id))
            if (account1_type == 2):
                accounts.append(savings_account(account1_name, account1_balance, account1_password, id))
            account.show(self, accounts)
        if (menu_input == 2):
            account.change_balance(self, accounts)
        if (menu_input == 3):
            account.show_balance(self, accounts)
        if (menu_input == 4):
            self.running = False
        if(menu_input != 1 or 2 or 3 or 4):
            return None
if __name__ == '__main__':
    
    main = main()
    accounts = []
    print(len(accounts))
    while (main.running == True):
        main.menu(accounts)






