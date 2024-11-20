 # Write a program where the user has to gues a secret 
 # between 1 and 10. The program should provide feedback 
 # if the guess is too high or too low and congratulate 
 # the user if they guess it correctly. 

import random
secret_num = random.randint(1, 10)
guess_num = int(input("Pick a number between 1 and 10: "))
if (guess_num == secret_num):
    print("Congratulations, you guessed it!")
elif (guess_num < secret_num):
    print("Too low")
else:
    print("Too high")