import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()
for position in range(0, len(chosen_word)):
    letter = chosen_word[position] 
    if letter == guess:
        display[position] = letter
print(display)
