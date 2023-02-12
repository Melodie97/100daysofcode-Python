import random
from art import logo

numbers = range(1, 101)
computer_guess = random.choice(numbers)

print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

def play_game():

    print(logo)

    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    continue_game = True
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    while continue_game:
        print(f"You have {attempts} attempts remaining to guess the number")
        if attempts == 0:
            print("You lose")
            continue_game = False
        else:
            guess = int(input("Make a guess: "))
            if guess > computer_guess:
                attempts -= 1
                print (f"Too high \nGuess again")
            elif guess < computer_guess:
                attempts -= 1
                print (f"Too low \nGuess again")
            else:
                print("You Win!")
                continue_game = False    
    

play_game()
