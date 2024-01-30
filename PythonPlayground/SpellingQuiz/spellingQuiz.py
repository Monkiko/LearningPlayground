import os

choice = str(input("Do you want to create a new spelling list? Y/N: "))

if choice == "Y":
    
    if os.path.exists("spelling_list.txt"):
        os.remove("spelling_list.txt")
    else:
        print("The spelling_list.txt file does not exist")
    
    listLength = int(input("Please indicate the number of words in your spelling list: "))

    i = 0
    spellingList = []
    while i < listLength:
        spellingList.append(str(input("Provide a word for the spelling list: ")))
        i+=1

    file = open('spelling_list.txt', 'w')

    for i in spellingList:
        file.write(i)

    file.close()