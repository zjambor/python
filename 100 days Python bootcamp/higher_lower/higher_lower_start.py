from art import logo, vs
from game_data import data
import random
import os

def get_random_account():
  return random.choice(data)

def format_account(account):
  name = account['name']
  description = account['description']
  country = account['country']
  follower = account['follower_count']
  return f"{name}, a {description}, from {country}, followers: {follower}"

def check_answer(answer, acc_a, acc_b):
  if acc_a > acc_b:
    return answer == 'a'
  else:
    return answer == 'b'

def game():
  clear = lambda: os.system('cls')
  clear()
  print(logo)

  score = 0
  should_continue = True

  while should_continue:
    acc_a = get_random_account()
    acc_b = get_random_account()
    
    print(f"Compare A: {format_account(acc_a)}")
    print(vs)
    print(f"Against B: {format_account(acc_b)}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    acc_a_follower = acc_a['follower_count']
    acc_b_follower = acc_b['follower_count']
    is_correct = check_answer(answer, acc_a_follower, acc_b_follower)
  
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You are right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      should_continue = False


game()