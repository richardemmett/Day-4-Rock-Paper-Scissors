rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_options = [rock, paper, scissors]

player_index=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
player_choice = game_options[player_index]
computer_index = random.randint(0,2)
computer_choice = game_options[computer_index]

if player_choice == computer_choice:
  print (f"You chose {player_choice} and the computer chose {computer_choice}. It's a draw!")
elif (player_choice == rock and computer_choice == scissors) or (player_choice == paper and computer_choice == rock) or player_choice == scissors and computer_choice == paper:
  print (f"You chose {player_choice} and the computer chose {computer_choice}. You win!")
else:
  print (f"You chose {player_choice} and the computer chose {computer_choice}. You lose!")

