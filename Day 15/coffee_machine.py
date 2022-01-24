from coffee_data import MENU, resources, prices
machine_on = True

def check_user_input(user_input):
    money = 0
    if user_input == 'prices':
        for i in prices:
            print(f"{i} : ${prices[i]}")
    elif user_input == 'report':
        for i in resources:
            print(f"{i} : {resources[i]}")
        print(f"Money :${money}")
    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        print("Please insert coins")
        quaters_coin = int(input("How many quaters?: "))
        dimes_coin = int(input("How many dimes?: "))
        nickles_coin = int(input("How many nickels?: "))
        pennies_coin = int(input("How many pennies?: "))

        total_dollars = (quaters_coin * 0.25) + (dimes_coin * 0.10) + (nickles_coin * 0.05) + (pennies_coin * 0.01)
        if user_input == 'espresso':
            if total_dollars > 1.5:
                change = round(total_dollars - 1.5, 2)
                print(f"Here is ${change} in change \nHere is your espresso. Enjoy!")
                money += 1.5
            if total_dollars == 1.5:
                print("Here is your espresso. Enjoy!")
                money += 1.5
            else:
                print("Sorry you don't have enough money. Here's a refund.")

        elif user_input == 'latte':
            if total_dollars > 2.5:
                change = round(total_dollars - 2.5, 2)
                print(f"Here is ${change} in change \nHere is your espresso. Enjoy!")
                money += 2.5
            if total_dollars == 2.5:
                print("Here is your espresso. Enjoy!")
                money += 2.5
            else:
                print("Sorry you don't have enough money. Here's a refund.")

        elif user_input == 'cappuccino':
            if total_dollars > 3.0:
                change = round(total_dollars - 3.0)
                print(f"Here is ${change} in change \nHere is your espresso. Enjoy!")
                money += 3.0
            if total_dollars == 3.0:
                print("Here is your espresso. Enjoy!")
                money += 3.0
            else:
                print("Sorry you don't have enough money. Here's a refund.")

def check_resources():
    print(resources)
    #still have to code up this one, but would do this later


while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino) \nTo check prices, type prices \nTo check available resources, type report \n").lower()
    if user_input == "off":
        machine_on = False
    else:
         check_user_input(user_input=user_input)
