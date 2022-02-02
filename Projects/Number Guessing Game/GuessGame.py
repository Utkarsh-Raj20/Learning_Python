import random
import math

lower = int(input("input lower bound:"))
upper = int(input("input upper bound:"))

number = int(random.randint(lower, upper))
guess = int(input("Guess a number:"))
count = 1
while guess != number:
    count += 1
    if guess > number:
        print("Try Again, You guessed too high!")
        guess = int(input("Guess a number:"))
    else:
        print("Try Again, You guessed too small!")
        guess = int(input("Guess a number:"))
if guess == number:
    print("Congratulations You did it in " + str(count) + " tries")
