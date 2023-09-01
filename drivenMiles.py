mileage = 0.0

def main():
    mileage = getMileage()
    print("You've driven a total of ", mileage, "miles.")
    
def getMileage():
   mileage = float(input("Enter your vehicle's mileage: "))
   return mileage
   
main()
