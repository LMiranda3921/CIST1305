# This program determines if a bonus should be awarded

# The main function
def main():
    print('Welcome to the program')
    monthlySales = getSales()  # gets sales
    enough4Bonus(monthlySales)
    dayOff(monthlySales)
    
# This function gets the monthly sales
def getSales():
    monthlySales = float(input('Enter the monthly sales $'))
    return monthlySales

#this functions sees whether you you get a bonus
def enough4Bonus(monthlySales):
    if monthlySales >= 100000:
        print("You get a bonus of $5,000!!!")

#this function sees whether you get a day off 
def dayOff(monthlySales):
    if monthlySales >= 112500:
        print("You get a day off!!! Woohoo!")

# calls main
main()
