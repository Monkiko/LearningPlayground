import os

choice = str(input("Do you want to create a new spelling list? Y/N: "))

if choice == "Y" or choice == "y":
    
    if os.path.exists("spelling_list.txt"):
        os.remove("spelling_list.txt")
    
    listLength = int(input("Please indicate the number of words in your spelling list: "))

    i = 0
    makeSpellingList = []
    while i < listLength:
        makeSpellingList.append(str(input("Provide a word for the spelling list: ")))
        i+=1

    file = open('spelling_list.txt', 'w')

    for i in makeSpellingList:
        file.write(f"{i}\n")

    file.close()

elif choice == "N" or choice == "n":
    spelling_file = open("spelling_list.txt", "r")

    spellingList = []
    spellingList = spelling_file.readlines()

    spelling_file.close()

    for i in spellingList:
        print(i, end ="")

else:
    print("Incorrect Input. Please enter either 'Y' or 'N'")