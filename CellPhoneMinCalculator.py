def main():
    endProgram = "no"
    while endProgram == "no":
        minutesAllowed = 0
        minutesUsed = 0
        totalDue = 0
        minutesOver = 0
        
        minutesAllowed = getAllowed(minutesAllowed)
        minutesUsed = getUsed(minutesUsed)
        totalDue = calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver)
        minutesOver = calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver)
        printData(minutesAllowed, minutesUsed, totalDue, minutesOver)
        endProgram = str(input("Do you want to end program? yes or no: "))
        while endProgram != "yes" or endProgram != " no":
            print("Please enter yes or no. ")
            endProgram = str(input("Do you want to end program? yes or no. "))


def getAllowed(minutesAllowed):
    minutesAllowed = int(input("How many minutes are allowed? "))
    while minutesAllowed < 200 or minutesAllowed > 800:
        print("Please enter minutes bewteen 200 and 800.")
        minutesAllowed = int(input("How many minutes are allowed? "))
    return minutesAllowed


def getUsed(minutesUsed):
    minutesUsed = int(input("How many minutes were used? "))
    while minutesUsed < 0:
        print("Please enter in minutes of at least 0.")
        minutesUsed = int(input("How many minutes were used? "))
    return minutesUsed
    
    
def calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver):
    extra = 0.0
    if minutesUsed <= minutesAllowed:  
        totalDue = 74.99
        minutesOver = 0
        print("You were not over your minutes for the month. Wohoo")
    else:
        minutesOver = minutesUsed - minutesAllowed
        extra = minutesOver * .20
        totalDue = 74.99 + extra
        print("You were over your minutes by", minutesOver)
    return totalDue
    


def printData(minutesAllowed, minutesUsed, totalDue, minutesOver):
    print("-----------MONTHLY SALES REPORT--------------")
    print("Minutes allowed were ", minutesAllowed)
    print("Minutes used were ", minutesUsed)
    print("Minutes over were ", minutesOver)
    print("Total due is $", totalDue)
    
    
main()
    
    
    
