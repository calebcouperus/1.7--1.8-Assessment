"""Integer Checker v1
Checks input to make sure its a valid integer between 1 and 10"""

# Asks user for an integer between 1 and 10
integer = int(input("Enter and integer between 1 and 10\n"
                    ">>> "))

# If valid integer output 'program continues'
if 0 < integer < 11:
    print("Program Continues")

# else show error
else:
    print("Please enter a valid number/integer")
