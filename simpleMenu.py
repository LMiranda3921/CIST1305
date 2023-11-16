def menu():
    print("Welcome to the menu!")
    print("Please slect the option of your choice")
    print("1) Add new entry for today")
    print("2) View Entries.")
    print("3) You can exit.")

choice = input("Your selection")

if choice =="1":
    print("Adding your new entry for today.")
elif choice == "2":
    print("Viewing entries.")
elif choice == "3":
    print("Exiting.")
else:
    print("That is a invalid selection.")
menu()
