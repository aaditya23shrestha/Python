print("........CALCULATOR........")

while True:
    print(".........................")
    print("Choose your operation:\n")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Remainder (%)")
    print("6. Power (**)")
    print("7. Quotient (//)")
    print("8. Even/Odd check")
    print("9. Exit" )

    choice = int(input("Enter your choice(1-9): "))

    if choice == 9:
        print("Calculator closed")
        break
    if choice <1 or choice > 9:
        print("Invalid number")
        break

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    if choice == 1:
        add = n1+n2
        print(f"Addition result is{add}")
    elif choice == 2:
        sub = n1-n2
        print(f"Subtraction result is {sub}")
    elif choice == 3:
        mul = n1*n2
        print(f"Multiplication result is {mul}")
    elif choice == 4:
        div = n1/n2
        print(f"Division result is {div}")
    elif choice == 5:
        rem = n1%n2
        print(f"Remainder result is {rem}")
    elif choice == 6:
        power = n1**n2
        print(f"Power result is {power}")
    elif choice == 7:
        quo = n1//n2
        print(f"Quotient result is {quo}")
    elif choice == 8:
        if n1%2 == 0:
            print(f"{n1} is an even number.")
        else:
            print(f"{n1} is an odd number.")
        if n2%2 == 0:
          print(f"{n2} is an even number.")
        else:
            print(f"{n2} is an odd number.") 
