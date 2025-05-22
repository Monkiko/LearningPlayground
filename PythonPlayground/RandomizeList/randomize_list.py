from random import shuffle

word_list = []

list_length = int(input("How many words are in the list? "))

count = 0
while count < list_length:
  word = input("Please add word #" + str(count + 1) + ": ")
  word_list.append(word)
  count += 1

shuffle(word_list)
print(word_list)