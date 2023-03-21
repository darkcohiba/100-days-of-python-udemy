


print("Welcome to the secret auction program.")

def find_highest_bid(bids):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    print(f"The winning bid is {highest_bid}!")
    print(f"Congratulations goes to {highest_bidder}")


bids ={}
more_bidders = True
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    continue_option = input("Are there any other bidders? \n (yes/no): ")
    if continue_option == "no":
        more_bidders = False


find_highest_bid(bids)
# print(bids)