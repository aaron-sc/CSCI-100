import random
random.seed(2)

totals = {}

def roll_die(): # returns the total
    total = 0
    die = {1 : random.randint(1,6) , 2 : random.randint(1,6)}
    for d in die.keys():
        total += die[d]
    return total

for x in range(100):
    roll = roll_die()
    if(roll in totals):
        totals[roll] += "*"
    else:
        totals[roll] = "*"

totals_l = list(totals.keys())
totals_l.sort()

for total in totals_l:
    print(str(total) + "s: ", totals[total])