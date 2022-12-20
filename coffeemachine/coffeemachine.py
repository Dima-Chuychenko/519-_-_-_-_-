import sys
import time

print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")


class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.coffees = (1, 2, 3)

    def buy(self):
        buy_choose = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back to main manu: ")

        while buy_choose != '1' \
                and buy_choose != '2' \
                and buy_choose != '3' \
                and buy_choose != 'back':
            print("You wrote the wrong line!")
            buy_choose = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back to main manu: ")

        if buy_choose == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
                return None
            if self.coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
                return None
            if self.disposable_cups < 1:
                print("Sorry, not enough cups!")
                return None
            self.water = self.water - 250
            self.coffee_beans = self.coffee_beans - 16
            self.disposable_cups = self.disposable_cups - 1
            self.money = self.money + 4

        elif buy_choose == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
                return None
            if self.milk < 75:
                print("Sorry, not enough milk!")
                return None
            if self.coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
                return None
            if self.disposable_cups < 1:
                print("Sorry, not enough cups!")
                return None
            self.water = self.water - 350
            self.milk = self.milk - 75
            self.coffee_beans = self.coffee_beans - 20
            self.disposable_cups = self.disposable_cups - 1
            self.money = self.money + 7

        elif buy_choose == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
                return None
            if self.milk < 100:
                print("Sorry, not enough milk!")
                return None
            if self.coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
                return None
            if self.disposable_cups < 1:
                print("Sorry, not enough cups!")
                return None
            self.water = self.water - 200
            self.milk = self.milk - 100
            self.coffee_beans = self.coffee_beans - 12
            self.disposable_cups = self.disposable_cups - 1
            self.money = self.money + 6

        elif buy_choose == "back":
            return None

        print("I have enough resources, making you a coffee!\n")
        time.sleep(0.7)
        print("    /  ")
        time.sleep(0.7)
        print("    |  ")
        time.sleep(0.7)
        print("  █████")
        time.sleep(0.7)
        print("  ▼▲▼▲▼")
        time.sleep(0.7)
        print("   ▼▲▼ ")
        time.sleep(0.7)
        print("   ▀▀▀  \n")
        time.sleep(0.7)
        print("Take your espresso ♥\n")

    def fill(self):
        print("Write how many ml of water you want to add: ", end='')
        self.water = self.water + int(input())
        print("Write how many ml of milk you want to add: ", end='')
        self.milk = self.milk + int(input())
        print("Write how many grams of coffee beans you want to add: ", end='')
        self.coffee_beans = self.coffee_beans + int(input())
        print("Write how many disposable coffee cups you want to add: ", end='')
        self.disposable_cups = self.disposable_cups + int(input())

    def take(self):
        print("I gave you", self.money, "₴")
        self.money = 0

    def remaining(self):
        print(f'''The coffee machine has:
                  {self.water} of water
                  {self.milk} of milk
                  {self.coffee_beans} of coffee beans
                  {self.disposable_cups} of disposable cups
                  {self.money} of money\n''')

    @staticmethod
    def exit():
        print("Enjoy! Come back!")
        sys.exit()

    def action(self):
        while True:
            action_input = input("Write action (buy, fill, take, remaining, exit): ")
            while action_input != "buy" \
                    and action_input != "fill" \
                    and action_input != "take" \
                    and action_input != "remaining" \
                    and action_input != "exit":
                print("You wrote the wrong line!")
                action_input = input("Write action (buy, fill, take, remaining, exit):  ")
            if action_input == "buy":
                self.buy()
            elif action_input == "fill":
                self.fill()
            elif action_input == "take":
                self.take()
            elif action_input == "remaining":
                self.remaining()
            elif action_input == "exit":
                self.exit()


CoffeeMachine = CoffeeMachine()
CoffeeMachine.action()
