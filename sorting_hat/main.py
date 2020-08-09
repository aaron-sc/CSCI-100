import sys
# name: Aaron Santa Cruz
# class: csci100
# date: 8/9/2020
# project: Sorting Hat Activity
# sources: https://owlcation.com/humanities/Harrypotterhouses, https://www.verywellmind.com/the-big-five-personality-dimensions-2795422, https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

# Function to generate cool header
def generate_header(personality):
    return "-" + ("-"*len(personality)) + "-\n|"+personality+"|\n" + "-" + ("-"*len(personality)) + "-"

# Ask the question and increment (or not) based on the answer
def ask_question(question):
    answer = input("Question: Are you " + question + " (yes (y) or no (n)): ").lower()
    if(answer == "yes" or answer == "y"):
        return 1
    elif(answer == "no" or answer == "n"):
        return 0
    else:
        print(generate_header("NOT A VALID RESPONSE"))
        sys.exit(0)

# Find the largest val in the dict of scores and return it (or if there are multiple with the same score, return those as well)
def find_house(houses_and_scores):
    max_score_house = max(houses_and_scores, key=houses_and_scores.get)
    winners = []
    for houses in houses_and_scores:
        if(houses_and_scores[houses] == houses_and_scores[max_score_house]):
            winners.append(houses)
    return winners


# 5 Persoality Traits
personality_scores = ["openness", "extraversion", "conscientiousness", "agreeableness", "neuroticism"]

# Harry Potter Houses (Scores, they are balanced based on the number of different connections from each of the 5 big personality traits)
harry_potter_houses = {"gryffindor" : 1, "hufflepuff" : 6, "ravenclaw" : 0, "slytherin" : 3}

# 5 Persoality Traits (Connections)
personality_connections = {"openness" : {"creative" : "ravenclaw", "open to trying new things" : "ravenclaw", "someone who is focused on tackling new challenges" : "ravenclaw", "happy to talk about abstract concepts" : "ravenclaw" , "someone who often resists new ideas" : "gryffindor"}, "extraversion" : {"compulsive" : "gryffindor" , "a person who prefers isolation" : "ravenclaw", "someone who dislikes being the center of attention" : "ravenclaw"}, "conscientiousness" : {"someone who spends time preparing" : "ravenclaw","someone who has attention to detail" : "ravenclaw", "someone who likes a set schedule" : "ravenclaw" , "someone who often makes a lot of messes and isn't organized" : "slytherin", "someone who often fails to return things or put them back where they belong" : "slytherin", "someone who procrastinates often" : "gryffindor"}, "agreeableness" : {"someone who has a great deal of the interest of others" : "gryffindor", "someone who cares for others" : "gryffindor", "someone who feels empathy and concern for others" : "gryffindor" , "someone who takes little interest in others" : "slytherin", "someone who insults or belittles others":"slytherin", "someone who manipulates others" : "slytherin", "someone who doesn't care how people feel" : "slytherin"}, "neuroticism" : {"someone who experiences a lot of stress" : "hufflepuff", "anxious often" : "hufflepuff", "someone who experiences mood swings often" : "hufflepuff" , "someone who doesn't worry much" : "gryffindor"}}

# For loop to ask questions for each personality and increment the score
for personality in personality_scores:
    # Get the question
    questions = personality_connections[personality].keys()
    # Print the nice header
    print("\n"+generate_header(personality))
    # Ask each question
    for question in questions:
        # Increment (or don't) based on the answer
        harry_potter_houses[personality_connections[personality][question]] += ask_question(question)

# For loop that prints the final scores
for house in harry_potter_houses:
    print(house + ": " + str(harry_potter_houses[house]))

print("\nYou are most likely to be in the following house(s): ")
print(find_house(harry_potter_houses))
