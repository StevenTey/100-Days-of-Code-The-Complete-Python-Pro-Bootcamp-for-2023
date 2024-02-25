from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

def main():
    while True:
        choice = input(f"What would you like? ({menu.get_items()}): ")
        if choice == "off":
            break
        elif choice == "report":
            machine.report()
            money.report()
        else:
            drink = menu.find_drink(choice)
            if machine.is_resource_sufficient(drink):
                if money.make_payment(drink.cost):
                    machine.make_coffee(drink)

main()