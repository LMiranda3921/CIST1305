#Program is made to be like a blog, asking if the user wants to add a post or see posts made, or exit
#creating an array to hold every post made in the program
createdPosts = []
def menu():
    #the while loop will repeat the menu if it is true
    repeat = True
    while repeat == True:
        #showing menu
        print("\nWelcome to the Blog!")
        print("Please select the option.")
        print("1) Add a Post")
        print("2) View Posts.")
        print("3) Exit.")
        print(" ")
        #taking in the user's choice of the menu
        choice = int(input("Your selection: "))

        #It takes the input from user and choice a case depending on input 
        match choice:
            case 1:
                #goes to the getPost module to add a post to the array
                getPost()
            case 2:
                #goes to the viewPost module to view all the written posts in the array
                viewPosts()
            case 3:
                #makes the loop false, and stops asking for posts or viewing. 
                print("Exiting. Have a nice day!")
                repeat = False
            case _:
                #prints when user doesnt choose any of the available options
                print("That is a invalid selection.")

def getPost():
    #adds the inputed "post" into the empty array. adding onto it
    print("Adding new post.")
    post = str(input("Please enter in your entry:\n"))
    createdPosts.append(post)

def viewPosts():
    #lets you view all the input from the user placed in the array
    print(" ")
    print(createdPosts)
    
menu()

