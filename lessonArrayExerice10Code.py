def main():
    import random
    repeat = 0
    array = []
    saddlePoints = 0
    
    def arrayFunction():
        NUMROW = 7
        twoDArray = []
        value = 0
        randNum2 = 0
        row = 0

        while row < NUMROW:
            value = random.randint(0,20)
            twoDArray.append(value)
            row = row + 1 
        randNum2 = randNum2 + 1
        print(twoDArray)
        return twoDArray
    
    def findPoints(array):
        print("saddle points!")    
    
    while repeat < 7:    
        array = arrayFunction()
        findPoints(array)
        repeat = repeat + 1
        
    
        
main()
