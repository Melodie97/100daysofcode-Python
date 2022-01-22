
from game_data import data
from art import logo, vs
import random

data_length = range(0, len(data))

def random_person():
    return data[random.choice(data_length)]

person_one = random_person()
person_two = random_person()
if person_one == person_two:
    person_two = random_person()


continue_game = True
score = 0
while continue_game:
    print(logo)
    print(f"Compare A: {person_one['name']}, a {person_one['description']}, from {person_one['country']}")
    print(vs)
    print(f"Compare B: {person_two['name']}, a {person_two['description']}, from {person_two['country']}")
    
    user_choice = input("Who has more followers, 'A' or 'B'? ").lower()
    if user_choice != 'a' and user_choice != 'b':
        print('You have entered an invalid choice, You lose!')
        continue_game = False
    else:
        if user_choice == 'a':
            if person_one['follower_count'] > person_two['follower_count']:
                score += 1
                print(score)
                print(f"You're right! Current score: {score}")
                person_one = person_two
                person_two = random_person()
                if person_two == person_one:
                    person_two = random_person()
            else:
                print()
                print(f"You lose!, Final score {score}")
                continue_game = False
        else:
            if person_one['follower_count'] < person_two['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}")
                person_one = person_two
                person_two = random_person()
                if person_two == person_one:
                    person_two = random_person()
            else:
                print(f"You lose!, Final score {score}")
                continue_game = False
