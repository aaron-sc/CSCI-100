# Name: Aaron Santa Cruz
# Class: csci100
# Date: 8/5/2020 
# Project: Menu
# Sources: https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory, https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python

# Function to open the file 
def open_file(f_name):
    return open(f_name, "r")

# Function to print each word
def print_file(f):
    contents = f.read()
    for w in contents.split():
        print(w)

# Function that prints the number of words:
def print_words_in_file(f):
    contents = f.read()
    print("This file has " + str(len(contents.split())) + " words.")

# Function that prints the longest words in file
def print_longest_words_in_file(f):
    contents = f.read()
    longest_list = []
    longest_w = ""
    for w in contents.split():
        if(len(w) > len(longest_w)):
            longest_list = []
            longest_w = w
            longest_list.append(w)
        elif(len(w) == len(longest_w)):
            longest_list.append(w)
    for w in longest_list:
        print(w)

# Funtion to Disp menu
def print_menu():
    print("\n1. Print words from file\n2. Print number of words in file\n3. Print longest word(s) from file\n4. Quit\n\nChoice: ")

def quit():
    print("Thanks for using my program :)")

# Below finds all .txt files and adds them to the list txts
import glob, os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
txts = []
u_file = ""
for file in glob.glob("*.txt"):
    txts.append(file)

# choosing what file
if(len(txts)) == 1:
    # Select default
    print("Selecting " + str(txts[0]) + ", as it's the only .txt file")
    wanted = txts[0]

else:
    # Choose what .txt file to use
    print(txts)
    wanted = input("What file do you want to use? (from above): ")
    while wanted not in txts:
        print("Not a valid file!")
        wanted = input("What file do you want to use? (from above): ")
    print("Using the file " + str(txts[txts.index(wanted)]) + ".")
    

# Set u_file to the file object
u_file = txts[txts.index(wanted)]

# Choices choice:function
choices = {1 : print_file, 2 : print_words_in_file, 3 : print_longest_words_in_file}

print_menu()

u_choice = int(input())
while u_choice != 4:
    print()
    if (u_choice in choices or u_choice == 4):
        choices[u_choice](open_file(u_file))
    else:
        print("Not a valid choice")

    print_menu()
    u_choice = int(input())

quit()