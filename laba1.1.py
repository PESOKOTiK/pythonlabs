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

# 2 task
x = 0.0
print("x   |  y")
while x <= 4.0:
    y = x
    x += 0.5
    print(str(x) + " | "+str(y))
