#is a data structure that stores variables of the same data type

def main():
    getSales2()
    
def getSales2():
    sales = []
    total = 0
    count = 0
    for num in range(6):
        newSales = float(input("Please enter in a sale number:\n "))
        sales.append(newSales)
        print(sales)
        total = total + newSales
        count = count + 1
    print("$", total)
main()
    
    
