# Random Number Game
import random

low_num = 0
high_num = 100
answer = random.randint(low_num, high_num)
isRunning = True
guesses = 0

print("----- Random Number Guessing Game -----")
print(f"Select a number between {low_num} and {high_num}")
while isRunning:
    guess = int(input("Enter your guess: "))
    guesses += 1
    if guess < low_num or guess > high_num:
        print("You have gone out of the range")
    elif guess < answer:
        print("Too low")
    elif guess > answer:
        print("Too high")
    else:
        print("That is a correct answer")
        break
print(f"You have given the correct answer {guess} in {guesses} attempts")





