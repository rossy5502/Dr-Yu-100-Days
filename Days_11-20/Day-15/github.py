
from modls import MENU, resources

total_money = 0
turn_coffee_machine_on = True

def is_resource_sufficient(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        if resources[item] < amount:
            print(f"there is not enough {item}.")
            return False

def deduct_resources(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount

def process_coins():
    print("Please insert coins.")
    try:
        quarters = int(input("how many quarters?: ") or 0)
        dimes = int(input("how many dimes?: ") or 0)
        nickles = int(input("how many nickles?: ") or 0)
        pennies = int(input("how many pennies?: ") or 0)
    except ValueError:
        print("Invalid input. Defaulting to 0 for all coins.")
        quarters = dimes = nickles = pennies = 0
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${total_money}")

while turn_coffee_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        turn_coffee_machine_on = False
    elif choice == "report":
        report()
    elif choice in MENU:
        if is_resource_sufficient(choice):
            print(f"This will cost you ${MENU[choice]['cost']}")
            total = process_coins()
            if total >= MENU[choice]["cost"]:
                change = round(total - MENU[choice]["cost"], 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
                deduct_resources(choice)
                total_money += MENU[choice]["cost"]
            else:
                print(f"Sorry, that's not enough money. Money refunded ${total}.")
        else:
            print("Sorry, not enough resources to make that drink. Turning off the coffee machine.")
            turn_coffee_machine_on = False
    else:
        print("Invalid input, try again.")
