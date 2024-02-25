# TODO: Import modules
from menu import MENU, resources

# TODO: User Input function
def user_input():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "espresso":
        return user_input
    elif user_input == "latte":
        return user_input
    elif user_input == "cappuccino":
        return user_input
    elif user_input == "report":
        return user_input
    elif user_input == "off":
        return user_input
    else:
        print("Invalid input, please try again.")
        user_input()

# TODO: Resources Check function
def is_resource_sufficient(order_ingredients, resources):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
    

# TODO:Coin Calculate function
def process_coins(item):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_amount = quarters*0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total_amount >= MENU[item]["cost"]:
        change = round(total_amount - MENU[item]["cost"], 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    

# TODO: Coffee Machine Function
def coffee_machine():
    # Initial Resources
    initial_resources = resources
    initial_resources["money"] = 0
    is_continue = True
    
    while is_continue:
        input = user_input()
        if input == "report":
            print(f"Water: {initial_resources['water']}ml \
                  \nMilk: {initial_resources['milk']}ml \
                  \nCoffee: {initial_resources['coffee']}g \
                  \nMoney: ${initial_resources['money']}")
        elif input == "off":
            break
        else:
            resource_check = is_resource_sufficient(MENU[input]["ingredients"], initial_resources)
            if resource_check == False:
                continue
            else:
                coin_check = process_coins(input)
                if coin_check == True:
                    initial_resources["money"] += MENU[input]["cost"]
                    for item in MENU[input]["ingredients"]:
                        initial_resources[item] -= MENU[input]["ingredients"][item]
                    print(f"Here is your {input} ☕️. Enjoy!")
                else:
                    continue
                    
coffee_machine()