#this program calculates retail prices
#MARK_UP is a global constant
MARK_UP = 2.5

#main function
def main():
    #varaible to control the loop
    another = "y"
    #process one or more items
    while another == "y" or another == "Y":
        show_retail()
        
        #do this again?
        another = input("Do you have another item? " + "(Enter y for yes): ")
        
#The show retail function gets an item's wholesale
#cost and displays the item's retail price
def show_retail():
    #get the item's whole cost
    wholesale = float(input("Enter the item's wholesale cost: "))
    #vaidate the wholesale cost
    while wholesale < 0:
        print("ERROR: the cost cannot be negative.")
        wholesale = float(input("Enter the correct wholesale cost: "))
    
    #calculate the retail price   and next line displays the retail price
    retail = wholesale * MARK_UP
    print("The retail price is $", format(retail, '.2f'))
#calling main funciton    
main()
