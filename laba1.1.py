# 1 Task
a = int(input("Enter a: "))
b = int(input("Enter b: "))
x = 0
if a > b:
    x = a / b + 31
elif a == b:
    x = -25
else:
    x = (a * 5 - 1) / a

print("X = " + str(x))
print()
# 2 task
x = 0.0
print("x   |  y")
while x <= 4.0:
    y = x
    x += 0.5
    print(str(x) + " | "+str(y))
print()
# 3 task
n = 5
for i in range(1, n + 1):
    print(8*" ", end='')
    for j in range(i, 0, -1):
        print(j, end=' ')
    for k in range(n - i):
        print(' ', end=' ')
    print()
for i in range(1, n + 1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(1, n - i + 2):
        if k < n - i + 1:
            print(k, end=" ")
        else:
            print(k, end="")
    print()
