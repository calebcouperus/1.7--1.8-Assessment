"""Yes/No checker v3
yes no checker, checks input to make sure its valid
v3 put v2 into a while loop
Based off: Yes No checker v2.py"""

played_before = ""
while played_before != "x":

    # Asks user if they have played before
    played_before = input("Have you played before?: ").lower()

    # If yes output 'program continues'
    if played_before == 'yes' or played_before == 'y':
        print("Program continues")

    # If no output 'Show instructions'
    elif played_before == 'no' or played_before == 'n':
        print("Shows instructions")

    # Else show error
    else:
        print("Please enter 'yes' or 'no'"
              "")

    print(f"You entered '{played_before}'\n")
