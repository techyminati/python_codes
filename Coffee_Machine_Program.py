MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_start = True
money = 0


def check_resources(coffee):
    if resources['water'] >= MENU[coffee]['ingredients']['water']:
        if resources['coffee'] >= MENU[coffee]['ingredients']['coffee']:
            if resources['milk'] >= MENU[coffee]['ingredients']['milk']:
                return "sufficient"
            else:
                return "no milk"
        else:
            return "no coffee"
    else:
        return "no water"


def collect_money():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total


def deduct_resources(coffee, money_got):
    resources['water'] = resources['water'] - MENU[coffee]['ingredients']['water']
    resources['milk'] = resources['milk'] - MENU[coffee]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[coffee]['ingredients']['coffee']
    global money
    money += MENU[coffee]['cost']


while machine_start:
    start_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if start_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: ${money}")
    elif start_choice == "off":
        break
    elif start_choice == "espresso" or start_choice == "latte" or start_choice == "cappuccino":
        resources_value = check_resources(start_choice)
        if resources_value == "sufficient":
            # Go ahead and take in money
            money_inserted = collect_money()
            if money_inserted >= MENU[start_choice]['cost']:
                deduct_resources(start_choice, money_inserted)
                if money_inserted > MENU[start_choice]['cost']:
                    change = round((money_inserted - MENU[start_choice]['cost']), 2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {start_choice}. Enjoy!")
            elif money_inserted < MENU[start_choice]['cost']:
                print("Sorry there is not enough money.")
                print("Your money is refunded.")
        elif resources_value == "no milk":
            print("Sorry there is not enough milk.")
        elif resources_value == "no water":
            print("Sorry there is not enough water.")
        elif resources_value == "no coffee":
            print("Sorry there is not enough coffee.")
    else:
        print("Invalid input.")
