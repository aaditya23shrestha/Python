#Voting 
"""
age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You cannot vote.")
    """

#EVen or odd
'''
number = int(input("ENter any number:"))
if number % 2 ==0:
    print(f"{number} is an even number.")
else:
    print(f"{number} ia an Odd number.")
'''

#nested if-else condition
'''
number = int(input("ENter any number:"))
if number >= 0:
    if number % 2 ==0:
        print("Positive even number.")
    else:
        print("Positive odd number.")
else:
    print("It is a negative number.Please enter a positive number.")
'''
#elif 
"""
marks = int(input("Enter your mark: "))
if marks >= 80:
    print("A+ ayooo")
elif marks >= 70:
    print("A ayoo")
elif marks >= 60:
    print("B+ ayoo")
elif marks >= 50:
    print("B ayoo")
else:
    print("Lau fail vayo.")
"""
#Logiacl operators -> AND, OR, NOT

#AND operator
"""
percentage = int(input("Enter your mark: "))
if percentage >= 90 and percentage <= 100:
    print("A+ ayooo")
elif percentage >= 80 and percentage <= 90:
    print("A ayoo")
elif percentage >= 70 and percentage <= 80:
    print("B+ ayoo")
elif percentage >= 60 and percentage <= 70:
    print("B ayoo")
else:
    print("Lau fail vayo.")
"""

#OR operator
"""
age = int(input("Enter your age: "))
if age >= 18 or age == 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
"""

#NOT operator -> makes value opposite

a = True
b = not a 
print(b)


