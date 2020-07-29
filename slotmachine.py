import random
random.seed(2)

slot1, slot2, slot3 = random.randint(0,9),random.randint(0,9),random.randint(0,9)
slot = [slot1,slot2,slot3]

def replay():
    global slot1, slot2, slot3, slot
    slot1, slot2, slot3 = random.randint(0,9),random.randint(0,9),random.randint(0,9)
    slot = [slot1,slot2,slot3]
    return ""

def check_win(slot1, slot2, slot3, slot):
    if(slot.count(slot1) == 2):
        return "Matched 2!!"
    if(slot.count(slot1) == 3):
        return "Matched 3!!"
    if(slot.count(slot2) == 2):
        return "Matched 2!!"
    if(slot.count(slot2) == 3):
        return "Matched 3!!"
    if(slot.count(slot3) == 2):
        return "Matched 2!!"
    if(slot.count(slot3) == 3):
        return "Matched 3!!"
    return "Sorry you lost!"

going = True

while going:
    print("Python Slot Machine")

    for num in slot:
        print(num, end=" ")
    

    print("\n"+check_win(slot,slot2,slot3,slot))
    going = True if(input("Play again (y)?: \n").lower() == "y") else False
    print(replay())

print("Thanks for playing!")