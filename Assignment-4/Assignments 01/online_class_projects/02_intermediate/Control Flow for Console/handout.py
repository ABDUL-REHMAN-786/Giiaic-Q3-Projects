# We want you to gain more experience working with control flow and Booleans in Python. 
# To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer,
#  who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is 
# actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

import random

def play_round():
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"Your number is: {user_number}")
    guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").strip().lower()

    if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
        print(f"Correct! The computer's number was {computer_number}. You get a point!\n")
        return 1
    else:
        print(f"Wrong! The computer's number was {computer_number}. No points this round.\n")
        return 0

def high_low_game(rounds=3):
    print("Welcome to High-Low! Try to guess if your number is higher or lower than the computer's.\n")
    
    score = 0
    for _ in range(rounds):
        score += play_round()

    print(f"Game Over! Your final score is: {score}/{rounds}")

# Start the game
high_low_game()
# The game will play 3 rounds by default, but you can change the number of rounds by passing a different value to the high_low_game function.
# For example, high_low_game(5) will play 5 rounds.

