# Rock Paper Scissors
# It works like rock crushes scissors, scissors cut paper and paper covers rock

import random

print("----- ROCK PAPER SCISSORS GAME-----")
options = ("rock", "paper", "scissors")
attempts = 0
playing = True

while playing:
    computer = random.choice(options)
    user = input("Enter the options (rock or paper or scissors): ")

    print(f"Computer: {computer}")
    print(f"User : {user}")
    attempts += 1

    if computer == user:
        print("It is a tie!")
    elif computer == "rock" and user == "paper":
        print("You wins!")
    elif computer == "paper" and user == "scissors":
        print("You wins!")
    elif computer == "scissors" and user == "rock":
        print("You wins!")
        break
    else:
        print("Computer wins")
    play_again = input("Do you want to play again(y/n): ").lower()
    if not play_again == "y":
        playing = False
print(f"You have won the game in {attempts} attempts!")


