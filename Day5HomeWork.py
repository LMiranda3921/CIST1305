#Algorithmn workbench
def main(): 
    #algNum1()
    #algNum2()
    #algNum3()
    #algNum4()
    #algNum5()
    algNum6()

def algNum6():
    row = 0
    column = 0
    for row in range(10,):
        print(row)

            






def algNum5():
    nominator = 1
    denominator = 30
    total = 0.0
    for num in range(30):
        print(nominator, "/", denominator)
        nominator = nominator + 1
        denominator = denominator - 1
        total = (nominator / denominator)
    print(total)
    

def algNum1():
    product = 0
    while product < 100:
        num = int(input("Enter in a a number please: "))
        product = num * 10
        print(product)
    
def algNum2():
    continueLoop = "y"
    while continueLoop == "y":
        num1 = int(input("Enter in a number: "))
        num2 = int(input("Enter in another number:"))
        num1 = num1 + num2
        print(num1)
        print("Would you like to perform the operation again?")
        continueLoop = str(input("(Enter in y for yes) "))
    print("Okay, have a nice day!")
    
def algNum3():
    count = 0
    for count in range(101):
        print(count * 10)
        
def algNum4():
    count = 0
    numTotal = 0
    while count < 10:
        num = int(input("Enter in a number: "))
        count = count + 1
        numTotal = numTotal + num
    print(numTotal)    
    


main()
