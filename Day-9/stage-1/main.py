from art import logo
print(logo)

bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ").title()
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        print("\n" * 20)

winner = max(bids, key=bids.get) # Find the key with the maximum value
print(f"The winner is {winner} with a bid of ${bids[winner]}")