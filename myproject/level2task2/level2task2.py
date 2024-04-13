                     ##  Number Guesser  ##

import random
print("Welcome to Guessing game")
min_number=int(input("Staring value : "))
max_number=int(input("Ending value :  "))
print(f"You want to guess a number between{min_number} and {max_number}")
numb=random.randrange(min_number,max_number)
n= int(input("Enter a number that you guess: "))
if n == numb:
    print("Machine number",numb)
    print("Congraluation you won")
elif numb < n:
    print("Machine number",numb)
    print("Your guessing number is high")
else:
    print("Machine number",numb)
    print("Your guessing number is low")
    