# task 1

mylist = []
length = int(input("Enter length of list "))
for i in range(length):
    element = input("Enter element ")
    mylist.append(element)

new_list = mylist[1::2]
print(new_list)

# task 2
mylist.reverse()
print(mylist)

# task 3

text = input("Enter text ")
letters_set = set()
for char in text:
    if char.isalpha() and char.islower():
        letters_set.add(char)
punctuation_count = sum(1 for char in text if char in ".,?!-;:'\"()[]{}")
print("множина лiтер", len(letters_set))
print("кiлькiсть знакiв пунктуацiї", punctuation_count)
