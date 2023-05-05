"""Integer Checker v3
Based off Integer Checker v2.1
Puts v2.1 into a loop for easy testing"""

number = ""
# Sets up the loop
while number != 'x':
    # Asks user for an integer between 1 and 10
    number = (input("Enter and integer between 1 and 10\n"
                    ">>> "))
    # Convert number into integer
    try:
        number = int(number)
        # If integer is valid print 'Program continues'
        if 0 < number < 10:
            print("Program continues\n")
        # Error for if the integer isn't between 1 and 10
        else:
            print("ERROR - Please enter an integer between 1 and 10\n")

    # Error for invalid type of input eg.(float, string)
    except ValueError:
        print("ERROR - Please enter an integer\n")
