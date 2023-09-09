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