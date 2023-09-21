def main():
    name1 = str(input("Please enter in a name: "))
    name2 = str(input("Please enter in another name: "))
    together = addNames(name1, name2)
    print(together)
    
    
def addNames(nameOne, nameTwo):
    name2gether = nameOne + nameTwo 
    return name2gether
    
main()
