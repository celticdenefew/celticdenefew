import random
name = input("Hello, What is your name? ")
question = input("Please type your 'Yes' or 'No' question here: ")
answer = ""
random_number = random.randint(1,9)
## This is a test of the random number generator:
## print(random_number)
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not to tell you now"
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

## The following checks if there is a question asked. If not it sends back an error message

if question == "":
  print("You must ask a question!")

## The following checks if there is a string (name) in the variable name. If there isn't it will just print out the question
else:
  if not name == "":
    print(name, "asks", question)
    print("Magic 8-Ball's answer: " + answer)
  else:
    print("Magic 8-Ball's answer: " + answer)
