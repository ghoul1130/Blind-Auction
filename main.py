from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
print("Welcome to secret auction game")
auction_log = {}
bidding_finished = False

def highest_bidder(auction_log):
  highest_bid = 0
  winner = ""
  for bidder in auction_log:
    current_bid = auction_log[bidder]
    if current_bid > highest_bid:
      highest_bid = current_bid
      winner = bidder
  print(f"WINNER: {winner} ---> BID: {highest_bid}")

while not bidding_finished:
  name = input("What is your name? : ")
  bid = int(input("What's your bid? : $"))  
  auction_log[name] = bid
  choice = input("Are there any bidders? Type 'yes' or 'no' : ")
  if choice == "no":
    bidding_finished = True
    highest_bidder(auction_log)
  elif choice =="yes":
    clear()  