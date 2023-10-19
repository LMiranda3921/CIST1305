#is a data structure that stores variables of the same data type

def main():
    getSales()
    
def getSales():
    sales = [] #this array is empty and can be filled in later
    total = 0
    count = 0
    while count < 6:
        newSales = float(input("Please enter in a sale number:\n "))
        sales.append(newSales)
        print(sales)
        total = total + newSales
        count = count + 1
    print(total)

main()
    
    
