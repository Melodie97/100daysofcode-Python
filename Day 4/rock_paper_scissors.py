import random

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
print("Welcome to my Rock-Paper-Scissors game!!")

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if users_choice >= 3 or users_choice < 0:
    print("You typed an invalid number, You lose!")

else:
    items = [rock, paper, scissors]
    print(items[users_choice])
    computers_choice = random.choice(items)
    print(f"Computer chose: \n {computers_choice}")

    if users_choice == 0:
        if computers_choice == rock:
            print("Play again")
        elif computers_choice == paper:
            print("You lose!")
        else:
            print("You win!!")

    if users_choice == 1:
        if computers_choice == rock:
            print("You win!!")
        elif computers_choice == paper:
            print("Play again")
        else:
            print("You lose!")

    if users_choice == 2:
        if computers_choice == rock:
            print("You lose!")
        elif computers_choice == paper:
            print("You win!!")
        else:
            print("Play again")
