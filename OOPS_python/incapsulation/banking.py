class Bankaccount:
    def __init__(self, owner, initial_bal):
        self.owner = owner #public attribute
        self._routing_number = 12345 #protected attribute
        self.__bal= initial_bal # private arrtibute

    # GETTER : safe way to read private data
    def get_bal(self):
        return self.__bal

    #SETTER : validate data before changing it
    def deposit(self, amount):
        if amount > 0:
            self.__bal += amount
        else:
            print("Valid Deposit amount!")

account = Bankaccount("Prem sen", 10000)

print(account.owner)
print(account.get_bal())
account._routing_number = 54321
print(account._routing_number)
account.deposit(400000)
print(account.get_bal())