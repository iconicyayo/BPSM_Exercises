
#!/usr/bin/env python3

# define a function to ask questions and store answers
def ask_questions():

    # create an empty dictionary for the answers
    answers = {}

    # ask the user five questions using input()
    # store each answer with a descriptive dictionary key
    answers["name"] = input("What's your name? ")
    answers["age"] = input("How old are you? ")
    answers["colour"] = input("What is your favourite colour? ")
    answers["python"] = input("Do you like Python? ")
    answers["flat"] = input("The world is flat: True or False? ")

    # return the completed dictionary
    return answers


# define a function to respond to the answers
def give_feedback(answers):

    # retrieve the name using its dictionary key
    print("\nHello", answers["name"] + "!")

    # display the age and favourite colour
    print("You are", answers["age"], "years old.")
    print("Your favourite colour is", answers["colour"] + ".")

    # check the python answer using a conditional
    if answers["python"].lower() == "yes":
        print("Great! Python is useful for bioinformatics.")
    else:
        print("Hopefully Python will become more enjoyable!")

    # check the answer about the shape of the earth
    if answers["flat"].lower() == "false":
        print("Correct! The Earth is not flat.")
    else:
        print("The Earth is actually approximately spherical!")


# call the function to collect the user's answers
user_answers = ask_questions()

# pass the completed dictionary to the feedback function
give_feedback(user_answers)
