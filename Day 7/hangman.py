import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
lives = len(stages) - 1

display = []
for letter in chosen_word:
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position] 
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")
    print(stages[lives])
