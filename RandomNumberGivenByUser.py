def main():
    import random
    print("I will give you a random number from two numbers you give me.")
    start = int(input("Enter in the starting number: "))
    print(" ")
  
    print("The next number needs to be greater when the first number you gave me")
    end = int(input("Enter in the ending number: "))
  
    choose = random.randint(start, end)
    print(choose)
    
main()
