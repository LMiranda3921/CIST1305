def main():
    #ITs adding in the random function
    #The repeat variable will call the arrayFunction to make more arrays to create a table 
    import random
    repeat = 0
    array = []
    saddlePoints = 0
    totalPoints = 0
    
    def arrayFunction():
        NUMROW = 7
        twoDArray = []
        value = 0
        randNum2 = 0
        row = 0

        while row < NUMROW:
            #valeu is getting assigned a random number
            #Then it is added onto the existing twoDArray
            value = random.randint(0,20)
            twoDArray.append(value)
            row = row + 1 
        randNum2 = randNum2 + 1
        print(twoDArray)
        return twoDArray
    
    def findPoints(array):
        print("saddle points!")    
    
    while repeat < 7:
        #calls the fuction that makes arrays multiple times
        #it will then send that array to get checked for saddlepoints
        array = arrayFunction()
        saddlePoints = findPoints(array)
        print(saddlePoints)
        repeat = repeat + 1
        
        
main()
