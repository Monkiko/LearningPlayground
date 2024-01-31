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
        sleep(5)
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


def readSpellingList():
    
    with open("spelling_list.txt", "r") as spelling_file:
        spellingList = []
        spellingList = spelling_file.readlines()

    spelling_file.close()

    for i in spellingList:
        print(i, end="")


start()