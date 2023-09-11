from account import account
from checking_account import checking_account
from savings_account import savings_account


class main:
    def __init__(self):
        self.running = True
        account1 = account()
    
    def menu(self):
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
                self.account1 = checking_account(account1_name, account1_balance, account1_password)
            if (account1_type == 2):
                self.account1 = savings_account(account1_name, account1_balance, account1_password)
        if (menu_input == 2):
            self.account1.change_balance()
        if (menu_input == 3):
            self.account1.show_balance()
        if (menu_input == 4):
            self.running = False
        else:
            print("invalid input please try again")
            return None
if __name__ == '__main__':
    
    main = main()
    while (main.running == True):
        main.menu()






