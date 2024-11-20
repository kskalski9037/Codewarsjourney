# imports
import random
import time

# comments!!!! where yo would want take notes!!!

'''
multiline comments
I'm still in a comment!!!
'''

# loosely typed - python figures out what kind of value it is
welcome_message = "The 💣 will explode in three incorrect guesses. Will you survive?"
min_number = 1
max_number = 10
secret_number = random.randint(min_number, max_number)
is_correct = False 

print(welcome_message)
print(f"The correct number is between {min_number} and {max_number}")
print("You have three attempts. Good luck \"bwahahah!\" 🤖")
      
guess = int(input("Go ahead and make your first guess: "))

# 1st guess
if guess == secret_number:
    print("You guessed it on your first try. Sadly, no 💥 for you")
    is_correct = True
elif guess < secret_number:
    print("Too low! 👿 Try again!")
    print() #empty line
else:
    print("Too high! 😈 Try again!")
    print() # empty line

if not is_correct:
    guess = int(input("You're getting closer to your demise, make your second guess: "))

# 2nd guess
if guess == secret_number:
    print("You guessed it on your second try. Sadly, no 💥 for you")
    is_correct = True
elif guess < secret_number:
    print("Too low! 👿 Try again!")
    print() #empty line
else:
    print("Too high! 😈 Try again!")
    print() # empty line

if not is_correct:
    guess = int(input("You're getting closer to your demise, make your second guess: "))

