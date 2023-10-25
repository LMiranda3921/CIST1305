import numpy as np
import random

twoDArray = np.random.randint(0, 20, size = (7, 7))
print(twoDArray)
#Finding saddle points in the 2DArray
for numRow in twoDArray:
    numCol = 0
    minimumNum = np.amin(numRow)
    for index in range(len(numRow)):
        # comparing the minimum number to the row
        if minimumNum == numRow[index]:
            rowNumber = index
            #transposing table to make new row with column numbers
            #it flips the table around so the rows and coloumns swtic
            #but stay in the same position of the values around it
            reverseArray = twoDArray.transpose()
            maxNum = np.amax(reverseArray[rowNumber])
            if maxNum == minimumNum:
                print("The saddle points are:",minimumNum,'.')
            if maxNum != minimumNum:
                print('There are no saddle points.')
