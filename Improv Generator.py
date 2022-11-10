## Generates Yes, No, Yes and... type questions for RPG
## Pull in Random number generator
import random

## question = input("Please type your 'Yes' or 'No' question here: ")
answer = ""
random_number = random.randint(1, 8)
## This is a test of the random number generator:
## print(random_number)

## code to assign random number to an answer
if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "Yes, and something good happens."
elif random_number == 3:
    answer = "Yes, but there is a complication."
elif random_number == 4:
    answer = "Reply hazy, change parameters and try again."
elif random_number == 5:
    answer = "No, but something interesting happens"
elif random_number == 6:
    answer = "No, and something bad happens"
elif random_number == 7:
    answer = "No"
elif random_number == 8:
    answer = "Maybe, add a variable and try again."

else:
    answer = "Error"
print("""Welcome to the GM simulator for solo play.
Ask a 'Yes' or 'No' question and we will roll a d8 to give you the answer.""")
question = input("What is your question? ")
print("The dice rolled a", str(random_number) + ": " + str(answer))
