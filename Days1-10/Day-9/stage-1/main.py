from art import logo
print(logo)

bids = {}
continue_bidding=True
while continue_bidding:
    name = input("What is your name?: ").title()
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if should_continue == "no":
        continue_bidding = False
    elif should_continue == "yes":
        print("\n" * 20)

winner = ""
max_bid = 0
for name in bids:
    if bids[name] > max_bid:
        max_bid = bids[name]
        winner=name
#or use
#winner = max(bids, key=bids.get) # Find the key with the maximum value


print(f"The winner is {winner} with a bid of ${bids[winner]}")