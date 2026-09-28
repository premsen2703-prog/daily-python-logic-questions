class ATM:

    #static variable
    __counter = 1
    def __init__(self,name):
        #instance variable
        self.name = name
        self._pin = ""
        self.__balance = 0
        self.sno = ATM.__counter
        ATM.__counter = ATM.__counter+1

        self.menu()
    @staticmethod
    def get_counter(self):
        return ATM.__counter
    @staticmethod
    def set_counter(self,new):
        if type(new) == int:
            ATM.__counter = new
        else:
            print("not allowed")

    def menu(self):
        while True:
            user_input = input(f"""
Hello, Wellcome to {self.name}
How would you like to proceed?
1. Enter 1 to Create Pin
2. Enter 2 to Deposit Money
3. Enter 3 to Withdraw
4. Enter 4 to Check balance
5. Enter 5 to Get Pin
5. Enter 6 to Exit
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
                self.get_pin()
            elif user_input == "6":
                print(" Exit 6 ")
                break
            else:
                print("Invalid option! Please try again.")

    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin is created successfully!")

    def get_pin(self):
        print(self.__pin)
    
    def set_pin(self,new_pin):
        self.__pin = new_pin
        print(" Pin changed")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter your amount: "))
            self.__balance = self.__balance + amount
            print("Deposited successfully!")
        else:
            print("Invalid Pin!")

    def withdrow(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Withdrawal successfully!")
            else:
                print("Insufficient funds!")
        else:
            print("Invalid Pin!")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print(f"Your current balance is: {self.__balance}")
        else:
            print("Invalid pin!")

sbi = ATM("SBI")
hdfc = ATM("HDFC")
boi = ATM("BOI")

print(ATM.get_counter)

