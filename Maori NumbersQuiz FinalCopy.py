""""Final Copy
Complete tested program with all final components"""
import random

# List with all the questions
questions_answers = [("What number is 'Tahi' in english?: ", 1),
                     ("What number is 'Rua' in english?: ", 2),
                     ("What number is 'Toru in english?: ", 3),
                     ("What number is 'Wha' in english?: ", 4),
                     ("What number is 'Rima' in english?: ", 5),
                     ("What number is 'Ono' in english?: ", 6),
                     ("What number is 'Whitu' in english?: ", 7),
                     ("What number is 'Waru' in english?: ", 8),
                     ("What number is 'Iwa' in english?: ", 9),
                     ("What number is 'Tekau' in english?: ", 10)]
# Randomising order of questions
random.shuffle(questions_answers)


# Yes/No Checker Function
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
            print("\nPlease enter 'yes' or 'no'\n")


# Instructions
def instructions():

    # Instruction go in here...
    print("\n---How to Play---\n"
          "This is a maori quiz game for numbers 1-10\n"
          "Press <enter> to move to the next question\n"
          "Enter your answer and when you're sure its right press <enter>\n"
          "The quiz will tell you whether it was right or wrong,\nyou will also"
          " get a final score at the end.\n"
          "Press 'x' when prompted if you would like to exit at any time\n"
          ">>>")


# Integer Checker Function
def integer_checker(question, answer):
    # Sets up the loop
    while True:
        # Asks user for an integer between 1 and 10
        number = (input(question))
        # Convert number into integer
        try:
            number = int(number)
            # If the answer is correct
            if number == answer:
                return "Correct"
            # If the answer is incorrect
            else:
                return f"Incorrect, correct answer was {answer}"

        # Error for invalid type of input eg.(float, string)
        except ValueError:
            return "Incorrect - HINT: Answers are only integers"


# Main starts here
print("\n"
      "---Welcome to the Maori numbers Quiz---\n"
      "")

# Asking if they've played before
played_before = yes_no_checker("Have you played this Quiz before?: ")

# If they haven't played before show instructions
if played_before == "No":
    instructions()

# Rounds
round_number = 0
next_round = ""
score = 0
while next_round != 'x':
    next_round = input("\n"
                       "Next: <enter>\n"
                       "Quit: 'x'").lower()
    # To break the loop if they want to quit the game
    if next_round == 'x':
        break
    print(f"\nRound {round_number + 1}")
    correct_incorrect = integer_checker(questions_answers[round_number][0],
                                        questions_answers[round_number][1])
    print(f"\n{correct_incorrect}")
    if correct_incorrect == "Correct":
        # Scoring
        score += 1
    # keeping track of rounds
    round_number += 1
    # stops the game after 10 questions to avoid error
    if round_number == 10:
        break

# Final score and 'Goodbye'
print(f"\n"
      f"You scored {score}/{round_number}")
print("Thanks for playing\n"
      "---Goodbye---")
