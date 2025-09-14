from random import choice
from art import stages,logo
from words import word_list

lives = 6
#import the logo from art.py and display it
logo=logo
print(logo)
#import word list and use instead of the short world list we used previously
wordList = word_list
# Generate a random word from the word list
chosen_word = choice(word_list)
print(chosen_word)  # For testing
wordLength = len(chosen_word)
display = ["_"] * wordLength
print(' '.join(display))

game_over = False
while not game_over:
    guess = input("\nGuess a letter: ").lower()

    # Check if the guess is correct
    if guess in display:
        print("You've already guessed that letter.try again")
        print("no lives lost")

    elif guess in chosen_word:
        # Update display with all occurrences of the guessed letter
        for index in range(wordLength):
            if chosen_word[index] == guess:
                display[index] = guess


    elif guess not in chosen_word and guess not in display:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
        print(f"{guess} is not in the word.try again")

    # Print the current hangman stage (stages are in reverse order)
    print(stages[lives])

    # Print the current word state
    print(' '.join(display))

    # Check for win/lose conditions
    if "_" not in display:
        print("\nCongratulations! You've won!")
        game_over = True
    elif lives == 0:
        print("\nGame Over! You've run out of lives.")
        print(f"The word was: {chosen_word}")
        game_over = True
