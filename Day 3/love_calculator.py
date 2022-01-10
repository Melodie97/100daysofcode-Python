# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

#Calulate for TRUE
concatenated_names = name1_lowercase + name2_lowercase
total_true = concatenated_names.count("t") + concatenated_names.count("r") + concatenated_names.count("u") + concatenated_names.count("e")
string_total_true = str(total_true)

#Calculate for LOVE
total_love = concatenated_names.count("l") + concatenated_names.count("o") + concatenated_names.count("v") + concatenated_names.count("e")
string_total_love = str(total_love)

total = int(string_total_true + string_total_love)
if total < 10 or total > 90:
    print (f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
