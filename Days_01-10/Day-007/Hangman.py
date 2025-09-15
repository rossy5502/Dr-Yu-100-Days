from random import choice




# Generate a random word from the word list
word_list = ["apple", "banana", "cherry", "date", "berry"]
chosen_word = choice(word_list)
print(chosen_word)  # For testing
wordLength = len(chosen_word)
display = ["_"] * wordLength
print(' '.join(display))

game_over = False
while not game_over:
    guess = input("\nGuess a letter: ").lower()
    
    # Check if the guess is correct
    if guess in chosen_word:
        # Update display with all occurrences of the guessed letter
        for index in range(wordLength):
            if chosen_word[index] == guess:
                display[index] = guess
    else:

        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
    
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
