change = {"dollar" : 100, "quarter" : 25, "dime" : 10, "nickel" : 5, "penny" : 1}
amount_of_change = {"dollar" : 0, "quarter" : 0, "dime" : 0, "nickel" : 0, "penny" : 0}

amount_to_convert = int(input())

if(amount_to_convert <= 0):
    print("No change")

for change_type in change.keys():
    amount_of_change[change_type] = amount_to_convert // change[change_type]
    amount_to_convert %= change[change_type]


else:
    for change_type in amount_of_change.keys():
        if(amount_of_change[change_type] != 0):
            if(amount_of_change[change_type] == 1):
                print(str(amount_of_change[change_type]) + " " + change_type.title())
            else:
                if(change_type == "penny"):
                    print(str(amount_of_change[change_type]) + " " + "Pennies")
                else:
                    print(str(amount_of_change[change_type]) + " " + change_type.title() + "s")