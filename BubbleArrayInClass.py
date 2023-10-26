
def bubbleSort(array):
    #This program prints each element in the array seperately
    #for optimatized code, so if the code is already sorted
    #it doesnt need to go through the entire process
    n =len(array) 
    swapped = False
    #we are going through all the elements
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            return

        
array = [7, 2, 23, 8, 38, 1, 56, 3, 51, 9]

print("The original array is: \n", array)
bubbleSort(array)

#the for loop will keep looping in the For Each loop
#it doesnt need a counter variable as it already counts for you
print("Press enter for the sorted array: ")
for element in range(len(array)): 
    print("% d" % array[element], end = " ")
