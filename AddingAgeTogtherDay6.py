def main():
    firstAge = 0
    secondAge = 0
    total = 0

    firstAge = int(input("Enter your age. "))
    secondAge = int(input("Enter your best friend's age. "))

    total = sum(firstAge, secondAge)
    print("Together you are, ", total, " years old.")


def sum(num1, num2):
    result = num1 + num2
    return result
    
    
main()
