"""Yes/No checker v4
yes no checker, checks input to make sure its valid
v4 puts v3 Yes No checker into a function
Based off: Yes No checker v3.py"""


# function starts
def yes_no_checker(question_yes_no):
    while True:
        # Asks user if they have played before
        answer = input(question_yes_no).lower()

        # If yes output 'program continues'
        if answer == 'yes' or answer == 'y':
            answer = "Yes"
            return answer

        # If no output 'Show instructions'
        elif answer == 'no' or answer == 'n':
            answer = "No"
            return answer

        # Else show error
        else:
            print("Please enter 'yes' or 'no'")


# Main routine starts
show_instructions = yes_no_checker("Have you played this quiz before: ")
print(f"You entered '{show_instructions}'")
