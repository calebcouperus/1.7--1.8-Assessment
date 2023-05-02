"""Integer Checker v2
Based off Integer Checker v1
fixes issue where anything other than an integer entered crashes the program"""

# Asks user for an integer between 1 and 10
number = float(input("Enter and integer between 1 and 10\n"
                     ">>> "))

# If valid integer output 'program continues'
if number == 1 or number == 2 or number == 3 or number == 4\
        or number == 5 or number == 6 or number == 7 or number == 8\
        or number == 9 or number == 10:
    print("Program Continues")

# else show error
else:
    print("Please enter a valid number/integer")
