# by Liana Hill
# last updated October 21, 2019
# this program plays a number guessing game with the user

import random

def main():
    while True:
        answer = (input("Do you want to play a game? Answer with 'y' for yes or 'n' for no"))
        if answer == "y" or answer == "n":
            break
    if answer == "y":
        print("Great! Let's begin!")
    else:
        print("Processing...initiating Operation 'Terminate'")
    computer_number = random.randint(1, 100)
    int(input("Guess the computer's number")



main()