MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
profit = 0
is_on = True

def is_resource_sufficient(order_ingredients):
    """ Retursn true when the order of ingredients is available"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry  there is not enough {item}")
            return False
    return True

def process_coins():
    """ returns total calculated from coins inserted"""
    print('Please insert the coins: ')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.1
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total

def is_transaction_succesful(money_received, drink_cost):
    """ Return True when payment is accepted or false if insufficent"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is the ${change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry that is not enough')
        return False

def make_coffee(drink_name, order_ingredients):
    """dedeucted ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name}')



while is_on:
    intro = str(input('What would you like:? (Espresso, Latter or Cappuccino) '))
    if intro == 'off':
        is_on = False
    elif intro == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[intro]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_succesful(payment,drink["cost"]):
                make_coffee(intro, drink["ingredients"])

