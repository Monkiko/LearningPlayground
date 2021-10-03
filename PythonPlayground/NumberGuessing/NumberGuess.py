# Number Guessing Game
#
# Created by: Ian Rivera-Leandry
# Created on: 08-06-2021
# Last Revised on:  10-02-2021
#
#
from random import randrange
from os import system, name

def Clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def Randomize():
    global num
    num = randrange(101)


def Start():
    global response
    response = input("Guess a number between 1-100: ")
    InputCheck()


def InputCheck():
    global response
    global guess
    try:
        guess = int(response)
        NumGuess()
    except ValueError:
        print("Incorrect value entered.")
        Start()


def NumGuess():
    global guess
    global num
    if guess == num:
        print("You guessed correctly. Good job!")
        End()
    elif guess > num:
        print("OOPS! That was too high. Try again.")
        Start()
    elif guess < num:
        print("OOPS! That was too low. Try again.")
        Start()

def End():
    answer = input("Would you like to play again? (yes/no) ")
    if answer == "yes" or answer == "y":
        Clear()
        Randomize()
        Start()
    elif answer == "no" or answer == "n":
        print("Thank you for playing!")
    else:
        print("Invalid response. Answer with yes or no.")
        End()
            


print("Let's play a guessing game!")

Clear()
Randomize()
Start()