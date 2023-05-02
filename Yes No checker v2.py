"""Yes/No checker v2
yes no checker, checks input to make sure its valid
v2 fixes issue where 'y' and 'n' result in an error
also adds some more output
Based off: Yes No checker v1.py"""

# Asks user if they have played before
played_before = input("Have you played before?: ").lower()

# If yes output 'program continues'
if played_before == 'yes' or played_before == 'y':
    print("Program continues\n"
          "")

# If no output 'Show instructions'
elif played_before == 'no' or played_before == 'n':
    print("\n"
          "Shows instructions\n"
          "")

# Else show error
else:
    print("Please enter 'yes' or 'no'\n"
          "")

print(f"You entered '{played_before}'")
