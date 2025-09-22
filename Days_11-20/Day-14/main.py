import random
from art import logo, vs
from game_data import data
final_score=0

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, question_, question2_):
    if question_["follower_count"] > question2_["follower_count"]   :

        return guess=="A"
    else:
        return guess == "B"


question2 = random.choice(data)

while True:
    question = question2
    question2= random.choice(data)
    while question==question2:
        question2 = random.choice(data)
    print(logo)
    print("Compare A:", format_data(question))
    print(vs)
    print("Against B:", format_data(question2))
    answer = input("Who has more followers? A or B: ").upper()
    check_guess = check_answer(answer, question, question2)
    if check_guess:
        final_score = final_score + 1
        print(f"You got it! your current score is {final_score}")



    else:
            print(f"Sorry, that's wrong. your final score is {final_score}")
            print("GAME OVER")
            break



