# Dicts to hold val of each type of change
change = {"dollar" : 100, "quarter" : 25, "dime" : 10, "nickel" : 5, "penny" : 1}

# User's change
amount_of_change = {"dollar" : 0, "quarter" : 0, "dime" : 0, "nickel" : 0, "penny" : 0}

# Total change
amount_to_convert = int(input())

# No change
if(amount_to_convert <= 0):
    print("No change")

# Split the change
for change_type in change.keys():
    # Update the user's change
    amount_of_change[change_type] = amount_to_convert // change[change_type]
    # Update the change left over
    amount_to_convert %= change[change_type]

else:
    # For each type of change
    for change_type in amount_of_change.keys():
        # As long as there's change
        if(amount_of_change[change_type] != 0):
            # Singular coin
            if(amount_of_change[change_type] == 1):
                # Print the change
                print(str(amount_of_change[change_type]) + " " + change_type.title())
            else:
                # Check if a penny
                if(change_type == "penny"):
                    # Print it
                    print(str(amount_of_change[change_type]) + " " + "Pennies")
                else: # If not a penny
                    # Print it
                    print(str(amount_of_change[change_type]) + " " + change_type.title() + "s")