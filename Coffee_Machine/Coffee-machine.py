
Menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":100
    },
    
    "latte":{
        "ingredients":{
            "water":50,
             "milk":150,
            "coffee":18,
        },
        "cost":150
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
                "milk":100,

            "coffee":24,
        },
        "cost":200
    },
    
}
profit=0

resources={
"milk":800,
"water":800,
"coffee":300 
}

def check_resources(order_ingredients):
    for item in order_ingredients: #water milk coffee
        if order_ingredients[item]>resources[item]:
            print(f"Sorry ther is not enough {item}")
            return False
        return True
    
def process_coin():
    print("please insert coins")
    total=0
    five_rs=int(input("How many 5rs. coins : "))
    ten_rs=int(input("How many 10rs. coins : "))
    twenty_rs=int(input("How many 20rs. coins : "))
    total=(five_rs*5)+(ten_rs*10)+(twenty_rs*20)
    return total

def is_payment_successful(money_recieved,coffee_cost):
    
    if money_recieved>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=money_recieved-coffee_cost
        print(f"Here is your Rs.{change} in change ")
        return True
    else:
        print("Not sufficent money")
        return False

def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients :
        resources[item]-=coffee_ingredients[item]
    print(f"Here is your {coffee_name} ☕ ..Enjoy")

is_on=True
while is_on:
    print()
    choice=input("What would you like to have?(latte/espresso/cappuccino) : ").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water = {resources["water"]}ml")
        print(f"Milk = {resources["milk"]}ml")
        print(f"Coffee = {resources["coffee"]}ml")
        print(f"Money = Rs.{profit}")
    else:
        coffee_type=Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coin()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredients'])
            
            
    

