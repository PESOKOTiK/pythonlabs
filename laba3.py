mystring = "random text from my heart to my code and to all of its readers in the world"
tmpstring = mystring[19:(len(mystring)-1)]
for i in range(0, (len(tmpstring)-1), 4):
    print(tmpstring[i])
