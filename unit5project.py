# by Liana Hill
# last updated October 21, 2019
# this program plays a number guessing game with the user

import random


def main():
    # this while True loop allows the user to play the game multiple times
    while True:
        # this while True loop asks the user if they want to play a number guessing game
        while True:
            answer = (input("Do you want to play a game? Answer with 'y' for yes or 'n' for no"))
            if answer == "y" or answer == "n":
                break
        if answer == "y":
            print("Great! Let's begin!")
        else:
            print("Okay. See you next time!")
            break
        computer_number = random.randint(1, 100)
        tries = 0
        # this while True lets the user guess the computer's number and answers with the appropriate response;
        # it also tells the user the number of tries it took
        while True:
            user_guess = int(input("Guess the computer's number."))
            tries += 1
            if user_guess == computer_number:
                print("Correct! Great job!")
                break
            elif user_guess >= 100 or user_guess <= 0:
                print("Your number is not in the correct range of 1-100.")
            elif user_guess > computer_number:
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
        print("You guess the correct number in", tries, "tries")


main()
