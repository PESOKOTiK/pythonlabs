# Task 1
mystring = "random text from my heart to my code and to all of its readers in the world"
tmpstring = mystring[19:(len(mystring) - 1)]
for i in range(0, (len(tmpstring) - 1), 4):
    print(tmpstring[i])
# Task 2
myword = input("first word  ")
userword = input("user word  ")

ok = False
for letter in userword:
    if myword.find(letter) == -1:
        print("Not all letters are in my word")
        ok = False
        break
    else:
        ok = True

if ok:
    print("All letters are in my word")


