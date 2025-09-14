from art import logo


def caesar(text_, shift_, direction_):
    cipher_text = ""
    if direction_ == "decode":
        shift_ *= -1
    for letter in text_:
        if letter not in alphabet:
            cipher_text += letter
            continue
        new_position = (alphabet.index(letter) + shift_) % len(alphabet)
        cipher_text += alphabet[new_position]

    print(f"The {direction_}d text is {cipher_text}")


# Main program
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid direction. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart != 'yes':
        print("Goodbye!")
        break