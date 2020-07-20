house_prices = {}

i = 1
while i < 5:
    house_prices[i] = input("Please enter a price for house " + str(i) + ":\n")
    i += 1

print()

for house in house_prices.keys():
    print("The price of house of house " + str(house) + " is: $" + str(house_prices[house]))

print()

most_expensive = list(house_prices.values())
most_expensive = most_expensive.index(max((most_expensive)))

print("The most expensive house is: house " + str(most_expensive+1))

least_expensive = list(house_prices.values())
least_expensive = least_expensive.index(min((least_expensive)))
print("The least expensive house is: house " + str(least_expensive+1))
