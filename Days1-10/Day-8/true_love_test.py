def calculate_love_score(name1, name2):
    both_names = (name1 + name2).upper()
    score_true = 0
    score_love = 0

    # Count unique TRUE letters
    for letter in "TRUE":
        if letter in both_names:
            score_true += 1

    # Count unique LOVE letters
    for letter in "LOVE":
        if letter in both_names:
            score_love += 1

    print(f"Your love score is {score_true}{score_love}")


calculate_love_score("driss", "louise")