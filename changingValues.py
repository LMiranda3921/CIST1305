#main function
def main():
    value = 17
    changeValue(value)      #calling something, calling a different module
    print('The value is:', value)
    
    
def changeValue(value):
    value = 50
    print('The value is:', value)


main()
