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
    wordslens.append(len(word))

for num in newnums:
    numslens.append(len(num))

# Assign a combination of the length of each word and number to a random fortune
for word in wordslens:
    for num in numslens:
        chosenfortune = fortunes[random.randint(0,len(fortunes)-1)]
        combos[word+num] = chosenfortune
        fortunes.remove(chosenfortune)


# User inputs
while choosing:
    # Word
    print(newwords)
    user_word = input("Enter a word (from above): ").lower()
    if(user_word not in newwords):
        print("Not a valid word!")
        choosing = False
        break
    for letter in user_word:
        print(letter)
    user_len += len(user_word)

    # Num 1
    if(len(user_word) % 2 == 0):
        print(newnums)
        user_num1 = input("Enter a number (From above): ").lower()
        if(user_num1 not in newnums):
            print("Not a valid number!")
            choosing = False
            break
        for letter in user_num1:
            print(letter)
        user_len += len(user_num1)
    else:
        print(newnums2)
        user_num1 = input("Enter a number (From above): ").lower()
        if(user_num1 not in newnums2):
            print("Not a valid number!")
            choosing = False
            break
        for letter in user_num1:
            print(letter)
        user_len += len(user_num1)

    # num 2
    if(len(user_num1) % 2 == 0):
        print(newnums)
        user_num2 = input("Enter a number (From above): ").lower()
        if(user_num2 not in newnums):
            print("Not a valid number!")
            choosing = False
            break
        for letter in user_num2:
            print(letter)
        user_len += len(user_num2)
    else:
        print(newnums2)
        user_num2 = input("Enter a number (From above): ").lower()
        if(user_num2 not in newnums2):
            print("Not a valid number!")
            choosing = False
            break
        for letter in user_num2:
            print(letter)
        user_len += len(user_num2)

    # end the loop
    choosing = False
    showing_fortune = True

# Display fortune (if everyhting was entered)
if(showing_fortune):
    print("-"*65)
    print("Your fortune is: ")
    print(combos[user_len-3])