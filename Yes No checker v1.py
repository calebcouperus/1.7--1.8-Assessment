"""Yes/No checker v1
yes no checker, checks input to make sure its valid"""

# Asks user if they have played before
played_before = input("Have you played before?: ").lower()

# If yes output 'program continues'
if played_before == 'yes':
    print("Program continues")

# If no output 'Show instructions'
elif played_before == 'no':
    print("Shows instructions")

# Else show error
else:
    print("Please enter 'yes' or 'no'")
