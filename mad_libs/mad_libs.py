# name: Aaron Santa Cruz
# class: csci100
# date: July 8th 2020
# project: Mad Libs Activity
# sources: Story: https://usercontent1.hubstatic.com/7301022_f520.jpg, Resources: https://stackoverflow.com/questions/4628618/replace-first-occurrence-of-string-in-python, https://stackoverflow.com/questions/46106779/dictionary-value-as-function-to-be-called-when-key-is-accessed-without-using,https://stackoverflow.com/questions/39473297/how-do-i-print-colored-output-with-python-3

# Import a list of stories
from stories import stories
import random

# Class that allows for colored text :)
class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'



# Simple functions that gets rid of repitition and returns what the user enters

# Noun
def noun():
    return input("Please enter a noun: ")

# Boy's name
def b_name():
    return input("Please enter a boy's name: ")

# Girl's name
def g_name():
    return input("Please enter a girl's name: ")

# A season
def season():
    return input("Please enter a season: ")

# Adjective
def adj():
    return input("Please enter an adjective: ")

# Color
def u_color():
    return input("Please enter a color: ")

# Size
def size():
    return input("Please enter a size: ")

# Name
def name():
    return input("Please enter a name: ")

# Place of intrest
def poi():
    return input("Please enter a place of intrest: ")

# month
def month():
    return input("Please enter a month: ")

# type of bird
def type_of_bird():
    return input("Please enter a type of bird: ")

# room in a house
def room_in_house():
    return input("Please enter a room in a house: ")

# A cold food
def cold_food():
	return input("Please enter a cold food: ")

# Your name
def your_name():
	return input("Please enter your name: ")

# A food ending in s
def food_ending_in_s():
	return input("Please a enter a food that ends in s: ")

# past tense verb
def past_tense_verb():
    return input("Please enter a past tense verb: ")

# verb
def verb():
    return input("Please enter a verb: ")

# body part
def body_part():
    return input("Please enter a part of the body: ")

# An article of clothing
def article_of_clothing():
	return input("Please enter an article of clothing: ")

# Plural Noun
def p_noun():
    return input("Please enter a plural noun: ")

# Function to return the divider
def divider():
	return (color.BLUE + "-"*80 + color.END + "\n")

# User's story
story = stories[random.randint(0, len(stories)-1)]

# Array to store the words from the story
words_in_story = []

# String to hold the revised story when all of the words have been replaced
revised_story = story

# Dict that holds the words that need to be replaced in the story. Each value in the key/value pair is the named function. It does not call the function. Adding ([params]) would call the function
words_to_replace = {"[adj]" : adj, "article_of_clothing" : article_of_clothing, "food_ending_in_s" : food_ending_in_s, "your_name" : your_name, "cold_food" : cold_food, "[b_name]" : b_name, "[name]" : name, "[season]" : season, "[u_color]" : u_color, "[size]" : size, "[g_name]" : g_name, "[month]" : month , "[type_of_bird]" : type_of_bird , "[room_in_house]" : room_in_house, "[past_tense_verb]" : past_tense_verb, "[verb]" : verb, "[body_part]" : body_part,"[p_noun]" : p_noun}

# Creates an array for the for loop to iterate over
replaceable_words = words_to_replace.keys()

# Welcome message
print(divider() + "Welcome to " + color.BLUE + "MAD LIBS!" + color.END + " I have selected a random story for you out of a list of " + str(len(stories)) + " stories!")

# For loop that takes each word that can be replaced in the story, checks to see if that word needs to be replaced, and if it does, revised story gets the FIRST instance of the word replaced
for word in replaceable_words:
	for word_s in story.split():
		if(word in word_s):
			print(color.BLUE + divider() + color.END)
			revised_story = revised_story.replace(word, color.GREEN + words_to_replace[word]() + color.END,1) #words_to_replace[word]() calls the function

# Print the notice
print(color.YELLOW + "NOTICE: All of your inputs are highlighted in " + color.END + color.GREEN + "green" + color.END + color.YELLOW + "!" + color.END)

# Print the story
print(color.BLUE + divider() + color.END + "\n" + revised_story)