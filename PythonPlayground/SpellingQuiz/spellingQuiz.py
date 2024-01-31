"""
The purpose of this program is to create a spelling list and then display it either immediately or during subsequent runs of the program.

Created by: Ian Rivera-Leandry
Last Updated: January 31, 2024
Version 2.0.1
"""

import os
from time import sleep

def start():
    choice = str(input("Do you want to create a new spellinglist? Y/N "))

    if choice.lower() == "y" or choice.lower() == "yes":
        askListLength()
    
    elif choice.lower() == "n" or choice.lower() == "no":
        readSpellingList()

    else:
        clean()
        print("Incorrect Input. Please enter either 'Y' or 'N'")
        sleep(3)
        start()


def clean():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def askListLength():
    listLength = int(input("Please indicate the number of words in your spelling list: "))
    createSpellingList(listLength)


def createSpellingList(listLength):
    
    if os.path.exists("spelling_list.txt"):
        os.remove("spelling_list.txt")

    i = 0
    makeSpellingList = []
    while i < listLength:
        makeSpellingList.append(str(input("Provide a word for the spelling list: ")))
        i+=1
    
    with open("spelling_list.txt", "w") as file:

        for i in makeSpellingList:
            file.write(f"{i}\n")
    file.close()

    askReadList()

def askReadList():
    seeList = str(input("Do you want to view the created list? Y/N "))

    if seeList.lower() == "y" or seeList.lower() == "yes":
        readSpellingList()
    
    elif seeList.lower() == "n" or seeList.lower() == "no":
        print("Ending program now...")
        sleep(3)
        exit()

    else:
        clean()
        print("Incorrect Input. Please enter either 'Y' or 'N'")
        sleep(3)
        askReadList()

def readSpellingList():
    
    with open("spelling_list.txt", "r") as spelling_file:
        spellingList = []
        spellingList = spelling_file.readlines()

    spelling_file.close()

    clean()

    for i in spellingList:
        print(i, end="")


start()