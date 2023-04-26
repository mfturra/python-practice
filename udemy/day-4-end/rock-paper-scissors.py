# import necessary libraries
import random

# Variables
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

# Gather user input
user_input = int(input(
    "What do you choose? Type 0 for rock, 1 for Paper, or 2 for Scissors: \n"))

# Print user selection
game_images = [rock, paper, scissors]

if user_input > 2:
    print("That's an invalid number. You lose!")
else:
    print((game_images[user_input]))

    # Randomize computer selection
    comp_choice = random.randint(0, 2)

    # Print algorithmic selection
    print(f"Computer chose: {comp_choice}")
    print(game_images[comp_choice])

    # Win, loss, and tie conditions with output
    if user_input >= 3 or user_input < 0:
        print("You typed an invalid number, you lose!")
    elif user_input == 0:
        if comp_choice == 0:
            print("You tied!")
        elif comp_choice == 1:
            print("You lose")
        else:
            print("You won!")
    elif user_input == 1:
        if comp_choice == 0:
            print("You win!")
        elif comp_choice == 1:
            print("You tied!")
        else:
            print("You lose!")
    elif user_input == 2:
        if comp_choice == 0:
            print("You lose")
        elif comp_choice == 1:
            print("You win!")
        else:
            print("You tied!")
