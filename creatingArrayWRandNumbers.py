import random
myArray = []

for index in range(5):
    number = random.randint(0, 100)
    myArray.append(number)

print(myArray)
print("The first element of this array is", myArray[0], ".")

print(" ")
add = int(input("Please add one more number to this array: "))
myArray.append(add)
print(myArray)
