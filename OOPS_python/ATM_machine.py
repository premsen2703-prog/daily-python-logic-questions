class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
Hello, How would you like to proceed?
1. Enter 1 to Create Pin
2. Enter 2 to Deposit Money
3. Enter 3 to Withdraw
4. Enter 4 to Check balance
5. Enter 5 to Exit
ENTER: """)
            
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdrow()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Exit")
                break
            else:
                print("Invalid option! Please try again.")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin is created successfully!")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter your amount: "))
            self.balance = self.balance + amount
            print("Deposited successfully!")
        else:
            print("Invalid Pin!")

    def withdrow(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdrawal successfully!")
            else:
                print("Insufficient funds!")
        else:
            print("Invalid Pin!")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your current balance is: {self.balance}")
        else:
            print("Invalid pin!")

sbi = ATM()
