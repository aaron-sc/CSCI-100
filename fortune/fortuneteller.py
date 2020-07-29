# name: Aaron Santa Cruz
# class: csci100
# date: 7/25/2020
# project: Fortune Teller Activity
# sources: If you reference internet help or people other than instructors please cite 

# pseudocode: 3 Lists - Each lists holds a whole bunch of words and numbers and fortunes and are used for random generation. 
# The dictionary will have the each key be the possible lengths (combinations) of each word/number. 
# The values are the possible fortunes.

# Error I got: I got a dictionary KeyError. The reason was because I had forgot that the len() function returns the length of the word (inclusive). Python is a zero based index.

from res import words, nums, fortunes
import random

# hold the lengths of the words/nums
wordslens, numslens = [], []

# var that loops the game
choosing = True

# var that decides wether or not to display a fortune!
showing_fortune = False

# var to hold lengths of chosen words/nums
previous_user_len = 0
user_len = 0

# Set these arrays for the words and nums that are randomly picked
newwords = []
newnums = []
newnums2 = []

# random words/colors (no repeats)
for x in range(0, 4):
    chosenword = words[random.randint(0, len(words)-1)]
    newwords.append(chosenword)
    words.remove(chosenword)

# random numbers (no repeats)
for x in range(0, 8):
    chosennum = nums[random.randint(0, len(nums)-1)]
    if(x % 2 != 0):
        newnums.append(chosennum)
    else:
        newnums2.append(chosennum)
    nums.remove(chosennum)


# Combined possible outcomes
combos = {} # len:fortune

for word in newwords:
    wordslens.append((len(word)-1))

for num in newnums:
    numslens.append((len(num)-1))


# Assign a combination of the length of each word and number to a random fortune
for word in wordslens:
    for i, num in enumerate(numslens):
        chosenfortune = fortunes[random.randint(0,len(fortunes)-1)]
        combos[word+num+len(newnums2[i])-1] = chosenfortune
        
        # DEBUGGING STATEMENT
        # print(str(word) + " + " + str(num) + " + " + str(len(newnums2[i])) + " = " + chosenfortune + " (" + str(word+num+len(newnums2[i])) + ")")

        fortunes.remove(chosenfortune)

def user_choices(words_list, user_type = "word"):
    global user_len, previous_user_len
    print(words_list)
    user_input = input("Enter a " + user_type + " (from above): ").lower()
    if(user_input not in words_list):
        print("Not a valid word!")
        return False
    else:
        for letter in user_input:
            print(letter)

        previous_user_len = user_len
        user_len += (len(user_input)-1)
        print(user_len)
        return True
    

# User inputs
while choosing:
    # Word
    choosing = user_choices(newwords, "word")

    if(choosing == False):
        break

    # Num 1
    if(((user_len+1)) % 2 != 0):
        choosing = user_choices(newnums, "number")
    else:
        choosing = user_choices(newnums2, "number")

    if(choosing == False):
        break

    # num 2
    if(((user_len-previous_user_len)+1) % 2 == 0):
        choosing = user_choices(newnums, "number")
    else:
        choosing = user_choices(newnums2, "number")
    
    if(choosing == False):
        break
    # end the loop
    choosing = False
    showing_fortune = True

print(combos)

# Display fortune (if everything was entered)
if(showing_fortune):
    print("-"*65)
    print("Your fortune is: ")
    if(user_len in combos):
        print(combos[user_len])
    else:
        print("An error occured")