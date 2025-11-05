""" Name: Natalie Cintron | Course: CSC 212 Data Structures | Project 2 |
This program reads a file that contains names of states and their corresponding
capitals. It is meant to allow the user to 1. get corresponding capital with the 
state entered and 2. allow them to participate in a learning game to guess the 
capital of a randomly selected state. 
"""
#import pydoc
import random #need this for the random number generator
#STEP 1
def filereader():
    states_capitals_file = open('capitals_of_states.txt', 'r')
    #opens capitals_of_states.txt file for reading
    line = states_capitals_file.readline() 
    states_and_capitals = {}
    #created empty dicitionary to store state/capital key-value pairs
    #a loop that stops at the end of the file
    while line != '':
        line = line.rstrip()
        #takes away \n from each line
        one_pair = line.split(', ')
        #splits each pair of state/capital from others BY THE COMMA so it includes two word states
        if len(one_pair) == 2:#2 because one for state and one for capital
            state = one_pair[1]#state is in index 1 as seen in the file
            capital = one_pair[0].strip(',')#capital is in index 0 
            #.strip(',')takes away this extra comma that was popping up
            states_and_capitals[state] = capital#makes the state the key and capital the value
        line = states_capitals_file.readline()
            #makes sure to read that line
    states_capitals_file.close()
    #closes file
    return states_and_capitals
    #needs to return information

#STEP 2
def main():
    states_and_capitals = filereader()
    #have to include this so main() knows what states_and_capitals is
    game = input("Would you like to play a game(Y/N)? ")
    #while loop to make first game  loop to tell what states and capitals are paired
    while game == 'Y':
        user_input = input("Please enter a state: ")

        if user_input in states_and_capitals:
            #uses [] to get value of key(user_input) in the dictionary
            print(f"The capital of {user_input} is {states_and_capitals[user_input]}")
        else: 
            print("The state is not in the database please try again.")

        answer = input("Would you like to enter another state (Y/N)? ")
        #if someone doesnt want to play/enters 'N' then loop breaks
        if answer != "Y": 
            break
##STEP 3
    state_names = list(states_and_capitals.keys())
    capital_names = list(states_and_capitals.values())
    #makes lists of the state/capital names using dictionary methods
##STEP 4
    learning = input("Would you like to play a learning game (Y/N)? ").strip().upper()

    if learning == 'Y':
        correct = 0
        incorrect = 0

        # loop 5 times
        for i in range(5):
            # pick a random index from 0–49 (change to len(state_names)-1 if list size changes)
            rand_number = random.randint(0, len(state_names) - 1)
            random_state = state_names[rand_number]
            
            guess = input(f"Type in the capital of {random_state}: ").strip()

            if guess.lower() == capital_names[rand_number].lower():
                print(f"You got that right! You have {4 - i} tries left!")
                correct += 1
            else:
                print(f"That was wrong! You have {4 - i} tries left!")
                incorrect += 1

        print("\nYou have completed the learning game!")
        print(f"You got {correct} capital(s) right and {incorrect} capital(s) wrong.")
    
    else: 
            print("Thanks for stopping by!") 
main()
#pydoc.writedoc('States_Capitals_Game')
