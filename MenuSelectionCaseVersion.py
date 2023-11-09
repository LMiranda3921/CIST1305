#cenitmeters = inches * 2.54
#meters = feet * 0.3048
#kilometers = miles * 1.609

#convert inches to centimeters
#convert feet to meters
#convert miles to kilometers
def main():

    # Display the menu
    print("--Main Menu--")
    print("1. Convert inches to centimeters.")
    print("2. Convert feet to meters")
    print("3. Convert miles to kilometers.")
    print("4. End Program")
    print()

    # Getting user selection
    menuSelection = int(input("Please choose a menu option: "))

    # Validating selection; change numbers to fit option amount
    while menuSelection < 1 or menuSelection > 4:
        print("That is an invalid selection.")
        menuSelection = int(input("Please choose a menu option: "))
    

    #Performing selected operation
    match menuSelection:
        case 1:
            convertToCenti()
        case 2: 
            convertToMeter()
        case 3:
            convertToKilo()
        case 4:
            print("Good Bye!")
        case _:
            print("Invalid selection.")

def convertToCenti():
    print(" ")
    print("Converting inches to centimeters.")
    inches = int(input("Enter in the number of inches you want to convert:\n"))
    centimeter = inches * 2.54
    print(float(centimeter), "centimeters") 

def convertToMeter():
    print(" ")
    print("Converting feet to meters.")
    feet = int(input("Enter in the number of feet you want to convert:\n"))
    meters = feet * 0.3048
    print(float(meters), "meters")

def convertToKilo():
    print(" ")
    print("Converting miles to kilometers.")
    miles = int(input("Enter in the number of miles you weant to convert:\n"))
    kilo = miles * 1.609
    print(float(kilo), "milometers")


main()

