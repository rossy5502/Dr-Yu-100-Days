import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > answer:
        print("Too high.")
        attempts -= 1
    elif guess < answer:
        print("Too low.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {answer}")
        break

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The number was {answer}")
    else:
        print("Guess again.")