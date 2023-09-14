#taking the users input and adding together. 
print("")    
keepGoing = "y"
number = 0
total = 0
count = 1
print("This program calculates the total of five numbers.")

while count <= 5:
    number = int(input(print("Enter a number: ")))
    total = total + number
    count = count + 1
print("The total of all the numbers is", total)
