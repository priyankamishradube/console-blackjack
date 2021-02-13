from replit import clear
import random
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
start_game = True
blackjack =""
start = input("Do you wish to play? y or n").lower()
print(logo)

def should_continue():
  should_continue = input("Do you wish to continue? y or n").lower()
  if should_continue == 'y':
    start_game = True
  else:
    start_game = False
    clear()

while start_game: 
  def calculate_score(f_card):
    f_score = 0
    for i in f_card:
      f_score +=i
    return f_score          

    if f_score == 21:
      return 0
    else:
      return f_score
    

  # user_card = random.choices(cards, weights=None, cum_weights=None, k=2)
  # comp_card = random.choices(cards, weights=None, cum_weights=None, k=2)

  user_card = [10,10,10]
  comp_card = [2,3]
  user = calculate_score(user_card)
  comp = calculate_score(comp_card)


  print(f"Your cards: {user_card}, current score: {user}")
  print(f"Computer's first card is : {comp_card[0]}")

  #test if anyone has a blackjack
  if user == 21:
    print('User has a blackjack, User WINS!!!')
  elif comp == 21:
    print('Computer has a blackjack. You LOSE :(')
    
  if user > 21:
    if 11 in user_card:
      user_card.remove(11)
      calculate_score(user_card)
     
