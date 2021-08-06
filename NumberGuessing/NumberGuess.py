# Number Guessing Game
#
# Created by: Ian Rivera-Leandry
# Created on: 08-06-2021
# Last Revised on: 
#
#
from random import randrange
from typing import TYPE_CHECKING
from os import system

num = randrange(101)

system('clear')

print("Let's play a guessing game!")
guess = int(input("Guess a number between 1-100: "))

def NumGuess():
    global guess
    if guess == num:
        print("You guessed correctly. Good job!")
    elif guess > num:
        print("OOPS! That was too high. Try again.")
        guess = int(input("Guess a number between 1-100: "))
        NumGuess()
    elif guess < num:
        print("OOPS! That was too low. Try again.")
        guess = int(input("Guess a number between 1-100: "))
        NumGuess()
    else:
        print("Incorrect value entered. Try a number between 1 and 100.")
        guess = int(input("Guess a number between 1-100: "))
        NumGuess()

NumGuess()