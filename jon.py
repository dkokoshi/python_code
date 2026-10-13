import random

# Generate a random number between 1 and 10
number = random.randint(1, 100000000000000
                        )

# Ask the user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Check if the guess is correct
if guess == number:
    print("You guessed it! 🎉")
else:
    print(f"Wrong! The number was {number}.")
