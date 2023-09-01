main()
print()
def joeBean():
    num1 = int(input("Give me a value: "))
    return(num1) 
    
def joeBrother():
    num1 = joeBean()
    num2 = int(input("Give me another value: "))
    print(num1 * num2)

joeBrother()
print()
