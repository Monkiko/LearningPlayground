# Number Guessing Game
#
# Created by: Ian Rivera-Leandry
# Created on: 08-06-2021
# Last Revised on:  08-06-2021
#
#
from random import randrange
from os import system, name

def Clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


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
    if guess == num:
        print("You guessed correctly. Good job!")
    elif guess > num:
        print("OOPS! That was too high. Try again.")
        Start()
    elif guess < num:
        print("OOPS! That was too low. Try again.")
        Start()

num = randrange(101)

print("Let's play a guessing game!")

Clear()
Start()