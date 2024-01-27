from game_data import data
from art import logo,vs
import random

def get_random_account():
  return random.choice(data)
Score = 0  
game_end = False
random_number = {}
random_number[0] = get_random_account()
new_values = random_number[0]
def compare_function(num1,num2):
    global Score
    if num1 > num2:
      Score+=1
      return 1
    else:
       return 0
def game_on():
  print(logo)
  global game_end, random_number, new_values
  while not game_end:
    random_number[0] = new_values
    random_number[1] = get_random_account()
    if random_number[0] != random_number[1]:
      print(f'\ncompare A: {random_number[0]["name"]}, a {random_number[0]["description"]}, from {random_number[0]["country"]}\n\n {vs} \nwith B: {random_number[1]["name"]}, a {random_number[1]["description"]}, from {random_number[1]["country"]}\n')
    
      user_input = input("\nWho has the highest followers \"A\" or \"B\": ").lower()
      if user_input == "a":
        cmp = compare_function(random_number[0]["follower_count"], random_number[1]["follower_count"])
      elif user_input == "b":
        cmp = compare_function(random_number[1]["follower_count"], random_number[0]["follower_count"])
      else:
        print("Please enter valid input\n")
        game_end = True 
      if cmp == 1:
         print(f"Your current score is {Score}")
         new_values = random_number[1]
      else:
         print("\nYou got this one wrong\n")
         print(f"You got {Score} correct! and your score is {Score}\n")
         game_end = True
    else:
        game_end = True
  
game_on()