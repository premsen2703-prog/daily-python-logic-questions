class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk 
        self.coffee = coffee
        self.cost = cost


class CoffeeMachine:
    def __init__(self):
        self.water = 300#(ml)
        self.milk = 200 #(ml)
        self.coffee = 100 #(g)
        self.money = 0#($)

    def report(self):
        print(f"""
        Water: {self.water}ml
        Milk: {self.milk}ml
        Coffee: {self.coffee}g
        Money: {self.money:.2f}$
        """)

    def is_resource_sufficient(self,drink):
        if self.water < drink.water:
            print("Sorry there is not enough Wter")
            return False
        if self.milk < drink.milk:
            print("Sorry theere is not enough Milk")
            return False
        if self.coffee < drink.coffee:
            print("Sorry there is not enough Coffee")
            return False
        return True 

    def process_coins(self, drink):
        print("Please insert coins.")
        total = int(input("How many quarters ($0.25)?: ")) * 0.25
        total += int(input("How many dimes ($0.10)?: ")) * 0.10
        total += int(input("How many nickels ($0.05)?: ")) * 0.05
        total += int(input("How many pennies ($0.01)?: ")) * 0.01

        if total < drink.cost:
            print("Sorry that's not enough money. Money refund.")
            return False

        change = total - drink.cost
        if change > 0:
            print(f"Here is ${change:.2f}in change.")

        self.money += drink.cost
        return True

    def make_coffee(self, drink):
        self.water -= drink.water
        self.milk -= drink.milk
        self.coffee -= drink.coffee
        print(f"Here is your {drink.name} ☕. Enjoy!")

    def run(self):
        menu = [
            MenuItem("espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem("latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem("cappuccino", water=250, milk=100, coffee=24, cost=3.0)
        ]

        is_on = True
        while is_on:
            choices = "/".join([item.name for item in menu])
            choice  = input(f"What would you like? ({choices} / report / off): ").lower()

            if choice == "off":
                is_on = False
            elif choice == "repost":
                self.report()
            else:
                drink = next((item for item in menu if item.name == choice),None)
                if drink:
                    if self.is_resource_sufficient(drink):
                        if self.process_coins(drink):
                            self.make_coffee(drink)
                else:
                    print("Invalid selection. Try again.")

if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run()



