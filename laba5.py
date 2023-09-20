n = int(input("Enter N "))
mas = []

for i in range(n):
    element = int(input("Enter mas number "))
    mas.append(element)

print("Max element is " + str(max(mas)))

# task 2
size = 7
mas = []
for i in range(size):
    row = [0] * size
    mas.append(row)

x = 1
for i in range(0, 7):
    for j in range(0, 7):
        if x+j <= 7:
            mas[i][j] = x+j
        else:
            mas[i][j] = 0

    x = x+1

for i in range(7):
    for j in range(7):
        print(mas[i][j], end=" ")
    print()


