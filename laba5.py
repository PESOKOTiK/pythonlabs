n = int(input("Enter N "))
mas = []

for i in range(n):
    element = int(input("Enter mas number "))
    mas.append(element)

max_element = max(mas)
print("Max element is " + str(max_element))
