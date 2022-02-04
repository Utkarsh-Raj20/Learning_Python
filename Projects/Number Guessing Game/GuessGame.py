import random
import math

lower = int(input("input lower bound:"))
upper = int(input("input upper bound:"))

number = int(random.randint(lower, upper))
tries = round(math.log(upper - lower + 1, 2))
print("You have only ", tries, " tries to guess the number")
guess = int(input("Guess a number:"))
count = 1
pas = True

while count < tries:
    if guess == number:
        print("Congratulations, You guessed the number in ", count, " tries")
        pas = False
        break
    elif guess > number:
        print("Try Again, You guessed too high!")
        guess = int(input("Guess a number:"))
    else:
        print("Try Again, You guessed too small!")
        guess = int(input("Guess a number:"))
    count += 1
if guess == number and pas:
    print("Congratulations, You guessed the number in ", count, " tries")
elif count > tries:
    print("The number was ", number)
    print("Better luck nexy time")
