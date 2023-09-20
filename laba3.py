# Task 1
while True:
    text = input("Введіть рядок, який має бути не менше 28 символів: ")
    if len(text) >= 28:
        break
    else:
        print("Рядок занадто короткий. Спробуйте ще раз.")
result = text[18::4]

print("Результат:", result)

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

# Task 3
mystring = "random text from my heart to my code and to all of its readers in the world"
wordlist = mystring.split(" ")
maxlen = len(wordlist[0])
maxstring = wordlist[0]
for word in wordlist:
    if maxlen < len(word):
        maxlen = len(word)
        maxstring = word

print("Max length word is " + maxstring + " with " + str(maxlen) + " Symbols ")
