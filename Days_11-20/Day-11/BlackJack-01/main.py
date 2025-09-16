from mods import create_deck,calculate_hand_value,display_hand


"""
Step 5: Game Logic
Implement the main game logic.
"""
def blackjack():
    print("Welcome to Blackjack!")
    deck_of_cards = create_deck()                 # Create a new deck of cards shuffled from the create_deck function

    # Initial hands
    player_hand = [deck_of_cards.pop(), deck_of_cards.pop()]
    dealer_hand = [deck_of_cards.pop(), deck_of_cards.pop()]

    # Player's turn
    while True:
        print("\nYour hand:")
        display_hand(player_hand)
        print("Dealer's hand:")
        display_hand(dealer_hand, hidden=True)

        player_value = calculate_hand_value(player_hand)
        print("Your hand value:", player_value)
        if player_value > 21:
            print("You busted! Dealer wins.")
            return

        choice = input("Do you want to [H]it or [S]tand? ").lower()
        if choice == 'h':
            player_hand.append(deck_of_cards.pop())
        elif choice == 's':
            break
        else:
            print("Invalid choice. Please choose 'H' or 'S'.")

    # Dealer's turn
    print("\nDealer's turn:")
    display_hand(dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck_of_cards.pop())
        print("Dealer hits:")

    dealer_value = calculate_hand_value(dealer_hand)
    player_value = calculate_hand_value(player_hand)

    # Determine the winner
    print("\nFinal Results:")
    print("Your hand:", player_value)
    display_hand(player_hand)
    print("Dealer's hand:", dealer_value)
    display_hand(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

"""
Step 6: Run the Game
Call the blackjack() function to start the game.
"""
if __name__ == "__main__":
    blackjack()
