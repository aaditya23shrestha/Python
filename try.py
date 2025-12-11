print("....CALCULATOR SAMPLE....")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Even/Odd chcek")
print("6. Power")
print("7. Remainder")
print("8. Quotient")
while True:
    choice = float(input("Choose any number between (1-8): "))
    if choice > 8 or choice < 1:
        print("Invalid. Please choose a number between (1-9).")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        add = a+b
        print(f"The additon of your question is {add}.")
    elif choice == 2:
        sub = a-b
        print(f"The subtraction of your question is {sub}.")
    elif choice == 3:
        div = a/b
        print(f"The division of your question is {div}.")
    elif choice == 4:
        mul = a*b
        print(f"The multiplication of your question is {mul}.")
    elif choice == 5:
        if a % 2 == 0:
            print("It is an even number.")
        else:
            print("It is an odd number.")  
        if b % 2 == 0:
            print("It is an even number.")
        else:
            print("It is an odd number.")      
    elif choice == 6:
        pow = a**b
        print(f"The power of your question is {pow}.")
    elif choice == 7:
        rem = a%b
        print(f"The remainder of your question is {rem}.")
    elif choice == 8:
        quo = a//b
        print(f"The quotient of your question is {quo} ")    


        


