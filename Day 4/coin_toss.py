import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
	 
random_toss = random.randint(0, 1)
if random_toss == "1":
    print("Heads")
else:
    print("Tails")
