  ## Guessing number game ##

import random
print("Welcome to Guessing game")
print("You want to guess a number from 1-100")
numb=random.randrange(1,101)
n= int(input("Enter a number that you guess: "))
if n > numb:
    print("Machine number",numb)
    print("Guessing number is high")
elif numb > n:
    print("Machine number",numb)
    print("Guessing number is low")
else:
    print("Machine number",numb)
    print("You won")

