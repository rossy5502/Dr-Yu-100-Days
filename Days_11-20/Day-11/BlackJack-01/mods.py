import random

"""
Step 2: Create a Deck of Cards
Create a function to generate a deck of cards.
"""
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'value': value, 'suit': suit} for suit in suits for value in values]
    random.shuffle(deck)
    return deck
"""
Step 3: Calculate Hand Value
Define a function to calculate the total value of a hand, accounting for Aces.
"""
def calculate_hand_value(hand):
    value = 0
    aces_counter = 0
    for card in hand:
        if card['value'].isdigit():                          # If the card is a number
            value += int(card['value'])                      # Add the card's value to the total
        elif card['value'] in ['Jack', 'Queen', 'King']:     # If the card is a face card
            value += 10                                      # turn the face card into a 10
        else:                                                # If the card is an Ace
            value += 11                                      # turn the Ace into a 11
            aces_counter += 1

    while value > 21 and aces_counter:
        value -= 10
        aces_counter -= 1

    return value

"""
Step 4: Display Cards
Create a function to display the cards in a hand.
"""
def display_hand(hand, hidden=False):
    if hidden:
        print("[Hidden Card],", *[f"{card['value']} of {card['suit']}" for card in hand[1:]])
    else:
        print(", ".join([f"{card['value']} of {card['suit']}" for card in hand]))

