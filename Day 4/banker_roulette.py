import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_names = len(names)
random_choice = random.randint(0, num_names-1)
print(f"{random_choice} is going to buy the meal today!")
