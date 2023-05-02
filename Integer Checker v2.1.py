"""Integer Checker v2.1
Based off Integer Checker v1
fixes issue where anything other than an integer entered crashes the program
Remove the need for a long list of valid integers"""

# Asks user for an integer between 1 and 10
number = float(input("Enter and integer between 1 and 10\n"
                     ">>> ")).__int__()

# If valid integer output 'program continues'
if 0 < number < 11:
    print("Program Continues")

# else show error
else:
    print("Please enter a valid number/integer")
