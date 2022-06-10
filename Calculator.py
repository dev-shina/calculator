while True :
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Modulus")
    print("Enter q or Q to Exit")

    choice = input("Enter your selection: ")

    if choice == "q" or choice == "Q" :
        break

    if choice in ("1","2","3","4","5"):

        val1 = float(input("Enter first value: "))
        val2 = float(input("Enter second value: "))

        if choice == "1" :
            print(val1, "+", val2, "=", (val1 + val2))

        elif choice == "2" :
            print(val1, "-", val2, "=", (val1 - val2))

        elif choice == "3" :
            print(val1, "*", val2, "=", (val1 * val2))

        elif choice == "4" :
            if val2 == 0.0:
                print("Divide by 0 Error")
            else:
                print(val1, "/", val2, "=", (val1 / val2))  

        elif choice == "5" :
            print(val1, "%", val2, "=", (val1 % val2))      

    else:
        print("Invalid choice, try again.")
        