
#Exercise 2
count = 5
while count <= 30:
    burned = count * 3.9
    print("In ", count, " minutes, you burn ", burned, " calories")
    count = count + 5


#Exercise 10
num = int(input("Enter in a number. If you want to stop, enter in -99.  "))
low = num
high = num

while num != -99:
    if num < low:
        low = num
    if num > high:
        high = num
    num = int(input("Enter in a number. If you want to stop, enter in -99.  "))
        
print("Smallest number is", low)        
print("Highest number is", high)
    
