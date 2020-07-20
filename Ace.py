import datetime
x = str(datetime.datetime.now())

inventory = {}

user_cart = {}

items = {1:"first", 2:"second", 3:"third"}

def add_to_inventory(item, price):
    global inventory
    inventory[item] = price

def add_to_cart(item, quantity):
    global user_cart
    user_cart[item] = quantity

i = 1
while i < 6:
    item = input("Please enter item " + str(i) + ":\n")
    price = float(input("Please enter the price of item " + str(i) + ":\n"))
    add_to_inventory(item, price)
    i += 1

print("\nWelcome to Ace Hardware!\n")

i = 0
while i < 3:
    item = input("What is the " + items[i+1]+ " item you would like to purchase?\n")
    quantity = int(input("How many would you like to purchase?\n"))
    add_to_cart(item, quantity)
    i += 1

print("\nThanks for shopping at Ace Hardware!\n"+x+"\n")

total = 0.0

for item in user_cart.keys():
    total += user_cart[item] * inventory[item]
    print(str(user_cart[item]) + " " + item + "(s) @ " + str(inventory[item]) + " = ${:0.2f}".format(user_cart[item] * inventory[item]))

print("\nYour total for today is: ${:0.2f}".format(total))