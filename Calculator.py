while True:

    print("============================")
    print("      PYTHON CALCULATOR")
    print("============================")
    
    Name = str(input("Enter Your Name: "))
    print("Welcome", Name)
    

    Num_1 = int(input("Enter your First Number: "))
    Num_2 = int(input("Enter your Second Number: "))

    print("\nChoose an operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")

    choice = input("\nEnter your Choice: ")

    print("\nYou have selected:", choice)

    if choice == '+':
        print("Your answer for Addition is:", Num_1 + Num_2)

    elif choice == '-':
        print("Your answer for Subtraction is:", Num_1 - Num_2)

    elif choice == '*':
        print("Your answer for Multiplication is:", Num_1 * Num_2)

    elif choice == '/':
        print("Your answer for Division is:", Num_1 / Num_2)

    else:
        print("Invalid Option Selected")

    again = input("\nDo you want to calculate again? (yes/no): ")

    if again == "no":
        print("Thank you", Name, "for using the calculator!")
        break
