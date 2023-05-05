"""Integer Checker v2.1
Based off Integer Checker v1
fixes issue where anything other than an integer entered crashes the program
Remove the need for a long list of valid integers
Also fixed that entering a string crashed v2"""

# Asks user for an integer between 1 and 10
number = (input("Enter and integer between 1 and 10\n"
                ">>> "))
# Convert number into integer
try:
    number = int(number)
    # If integer is valid print 'Program continues'
    if 0 < number < 10:
        print("Program continues")
    # Error for if the integer isn't between 1 and 10
    else:
        print("ERROR - Please enter an integer between 1 and 10")

# Error for invalid type of input eg.(float, string)
except ValueError:
    print("ERROR - Please enter an integer")
