from math import tan, sqrt


def func(x):
    x = int(x)
    return (2 * tan(x) - sqrt(x)) / x


print("Enter x ")
userx = input()
print("Z = ")
print(func(userx))