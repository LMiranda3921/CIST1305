def main():
    age = int(input("What is your age? "))
    income = float(input("What is your monthly income? "))
    name = input("What is your name? ")
    display(age, income, name) #I am sending these variables into display to use and come back with
    
    
def display(age, income, name):#() is holding the variables from main() to use in display
    print("Here are the variables:")
    print(age, " ", income, " ", name)
    
main()
