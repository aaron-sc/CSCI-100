# name: Aaron Santa Cruz
# class: csci100
# date: July 8th 2020
# project: Mad Libs Activity
# sources: Story: https://usercontent1.hubstatic.com/7301022_f520.jpg, Resources: https://stackoverflow.com/questions/4628618/replace-first-occurrence-of-string-in-python, https://stackoverflow.com/questions/46106779/dictionary-value-as-function-to-be-called-when-key-is-accessed-without-using

# Simple functions that gets rid of repitition and returns what the user enters

# Noun
def noun():
    return input("Please enter a noun: ")

# Adjective
def adj():
    return input("Please enter an adjective: ")

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

# past tense verb
def past_tense_verb():
    return input("Please enter a past tense verb: ")

# verb
def verb():
    return input("Please enter a verb: ")

# body part
def body_part():
    return input("Please enter a part of the body: ")

# Plural Noun
def p_noun():
    return input("Please enter a plural noun: ")

# User's story
story = "It was a [adj], cold [month] day. I woke up to the [adj] smell of [adj] [type_of_bird] roasting in the [room_in_house] downstairs. I [past_tense_verb] down the stairs to see if I could help [verb] the dinner. When I got there, I couldn't believe my [body_part]! There were [p_noun] all over the floor!"

# Array to store the words from the story
words_in_story = []

# String to hold the revised story when all of the words have been replaced
revised_story = story

# Dict that holds the words that need to be replaced in the story. Each value in the key/value pair is the named function. It does not call the function. Adding ([params]) would call the function
words_to_replace = {"[adj]" : adj , "[month]" : month , "[type_of_bird]" : type_of_bird , "[room_in_house]" : room_in_house, "[past_tense_verb]" : past_tense_verb, "[verb]" : verb, "[body_part]" : body_part,"[p_noun]" : p_noun}

# Creates an array for the for loop to iterate over
replaceable_words = words_to_replace.keys()

# For loop that takes each word that can be replaced in the story, checks to see if that word needs to be replaced, and if it does, revised story gets the FIRST instance of the word replaced
for word in replaceable_words:
	for word_s in story.split():
		if(word in word_s):
			print("-"*50)
			revised_story = revised_story.replace(word, words_to_replace[word](),1) #words_to_replace[word]() calls the function
 
# Print the story
print("-" * 50 + "\n" + revised_story)