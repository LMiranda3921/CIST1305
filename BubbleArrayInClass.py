
def bubbleSort(array):
    #This program prints each element in the array seperately
    #for optimatized code, so if the code is already sorted
    #it doesnt need to go through the entire process
    n =len(array) 
    swapped = False
    #we are going through all the elements
    for i in range(n-1):
        #range(n), also works but the outer loop
        #will repeat one more time than needed.
        #Last i elements are already in place
        for j in range(0, n-i-1):  #n-i-1 is just using the i in the above loop and subtract one from that loop
            #We go through the array from 0 to n-i-1
            #Swap if the element found is greater then the next element
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            #if we dont need to make a single swap, it will exit the main loop
            return

        
array = [7, 2, 23, 8, 38, 1, 56, 3, 51, 9]

print("The original array is: \n", array)
bubbleSort(array)

#the for loop will keep looping in the For Each loop
#it doesnt need a counter variable as it already counts for you
print("Sorted array is: ")
for element in range(len(array)): 
    print("% d" % array[element], end = " ")
