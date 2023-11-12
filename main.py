import art
import game_data
import random
import os

def clear():
  os.system("clear")

def random_choice():
  """ Random data from list"""
  return random.choice(game_data.data)

def formating_data(transofrmation_data):
  name = transofrmation_data["name"]
  description = transofrmation_data["description"]
  country =  transofrmation_data["country"]
  return f"{name}, a {description}, from {country}"

def comparing(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(art.logo)
  score = 0
  game_should_continue = True
  account_a = random_choice()
  account_b = random_choice()

  while game_should_continue:
    account_a = account_b
    account_b = random_choice()

    while account_a == account_b:
      account_b = random_choice()

    print(f"Compare A: {formating_data(account_a)}.")
    print(art.vs)
    print(f"Against B: {formating_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = comparing(guess, a_follower_count,  b_follower_count)

    clear()
    print(art.logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()


