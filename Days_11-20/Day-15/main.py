from modls import MENU
from modls import resources
turn_coffee_machine_on=True
total_money=0

def resources_deduction(coffee_type):
    ''' this function will deduct the resources used to make the coffee from the total resources available in the machine
    '''
    if coffee_type=="espresso":
        resources["water"]-=MENU["espresso"]["ingredients"]["water"]
        resources["coffee"]-=MENU["espresso"]["ingredients"]["coffee"]
    elif coffee_type=="latte":
        resources["water"]-=MENU["latte"]["ingredients"]["water"]
        resources["coffee"]-=MENU["latte"]["ingredients"]["coffee"]
        resources["milk"]-=MENU["latte"]["ingredients"]["milk"]
    elif coffee_type=="cappuccino":
        resources["water"]-=MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"]-=MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"]-=MENU["cappuccino"]["ingredients"]["milk"]

def resources_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${total_money}")

def coffee_making(espresso_, latte_, cappuccino_, ):
    ''' this function will check the machine resources available before accepting to make the coffee for the customer
    '''
    if espresso_:
        if resources["water"] >=MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >=MENU["espresso"]["ingredients"]["coffee"]:
         print(f"this will cost you ${MENU['espresso']['cost']} please insert coins")

    elif latte_:
        if resources["water"] >=MENU["latte"]["ingredients"]["water"] and resources["coffee"] >=MENU["latte"]["ingredients"]["coffee"]and resources["milk"] >=MENU["latte"]["ingredients"]["milk"]:
         print(f"this will cost you ${MENU['latte']['cost']} please insert coins")
    elif cappuccino_:
        if resources["water"] >=MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >=MENU["cappuccino"]["ingredients"]["coffee"]and resources["milk"] >=MENU["cappuccino"]["ingredients"]["milk"]:
         print(f"this will cost you ${MENU['cappuccino']['cost']} please insert coins")
    else:
        print("sorry there is not enough resources, turning off the machine")
        turn_coffee_machine_on=False


def coins():
    ''' this function will calculate the total amount of money inserted by the customer:
            '''

    try:
        quarters = int(input("how many quarters?: ") or 0)
        dimes = int(input("how many dimes?: ") or 0)
        nickles = int(input("how many nickles?: ") or 0)
        pennies = int(input("how many pennies?: ") or 0)
    except ValueError:
        print("Invalid input. Defaulting to 0 for all coins.")
        quarters = dimes = nickles = pennies = 0
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total




while turn_coffee_machine_on:
      customer_choice=input("what would you like? (espresso/latte/cappuccino): ").lower()
      
      if customer_choice == "espresso":
            coffee_making(espresso_=True, latte_=False, cappuccino_=False)#this function will check the machine resources available before accepting to make the coffee for the customer
            total=coins()#this function will calculate the total amount of money inserted by the customer
            if total>=MENU["espresso"]["cost"]:
                change=round(total-MENU["espresso"]["cost"],2)
                print(f"here is ${change} in change")
                print("here is your espresso ☕️. Enjoy!")
                resources_deduction("espresso")
                total_money+=MENU["espresso"]["cost"] #this will add the cost of the coffee to the total money
            else:
                print(f"sorry that's not enough money. Money refunded ${total}.")


      elif customer_choice == "latte":
            coffee_making(espresso_=False, latte_=True, cappuccino_=False)
            total=coins()
            if total>=MENU["latte"]["cost"]:
                change=round(total-MENU["latte"]["cost"],2)
                print(f"here is ${change} in change")
                print("here is your latte ☕️. Enjoy!")
                resources["water"]-=MENU["latte"]["ingredients"]["water"]
                resources["coffee"]-=MENU["latte"]["ingredients"]["coffee"]
                resources["milk"]-=MENU["latte"]["ingredients"]["milk"]

                total_money+=MENU["latte"]["cost"]
                resources_deduction("latte")
            else:
                print(f"sorry that's not enough money. Money refunded. {total}")


      elif customer_choice == "cappuccino":

          coffee_making(espresso_=False, latte_=False, cappuccino_=True)

          total = coins()

          if total >= MENU["cappuccino"]["cost"]:

              change = round(total - MENU["cappuccino"]["cost"], 2)

              print(f"here is ${change} in change")

              print("here is your cappuccino ☕️. Enjoy!")

              resources_deduction("cappuccino")

              total_money += MENU["cappuccino"]["cost"]

          else:

              print(f"sorry that's not enough money. Money refunded ${total}.")


      elif customer_choice == "report":
                    resources_report()
      elif customer_choice == "off":
            turn_coffee_machine_on=False
      else:
            print("invalid input try again")

