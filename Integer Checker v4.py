"""Integer Checker v4
Based off Integer Checker v3
Puts v3 into a function for use in final outcome"""


# question and answer both come from lists in the base
def integer_checker(question, answer):
    # Sets up the loop
    while True:
        # Asks user for an integer between 1 and 10
        number = (input(question))
        # Convert number into integer
        try:
            number = int(number)
            # If integer is valid print 'Program continues'
            if number == answer:
                print("Program continues\n")
            # Error for if the integer isn't between 1 and 10
            else:
                print("ERROR - Please enter an integer between 1 and 10\n")

        # Error for invalid type of input eg.(float, string)
        except ValueError:
            print("ERROR - Please enter an integer\n")


# Main starts
integer_checker("What is three: ", 3)
