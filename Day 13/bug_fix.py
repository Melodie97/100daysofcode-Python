# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#       #problem is that the range function doesn't include the last number
#     if i == 20:
#       print("You got it")
# my_function()
# # -------My Solution-----------
# def my_function():
#   for i in range(1, 21):
#       #problem is that the range function doesn't include the last number
#     if i == 20:
#       print("You got it")
# my_function()


# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_num) #error occurs when the random integer is 6
# print(dice_imgs[dice_num])
# --------My Solution-----------
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_num) #error occurs when the random integer is 6
# print(dice_imgs[dice_num])


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     #All conditions are false so code doesn't print an output
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# --------My Solution-----------
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#     #All conditions are false so code doesn't print an output
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")


# # Fix the Errors
# age = input("How old are you?") #no conversion of string to integer
# if age > 18:
# print("You can drive at age {age}.") #no indentation in the print statement and no use of f-string to call variable
#--------My Solution-----------
#   age = int(input("How old are you?"))
# # if age > 18:
# #     print(f"You can drive at age {age}.")


# # Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) #use of comparison operator instead of assignment operator
# total_words = pages * word_per_page
# print(total_words)
# --------My Solution-----------
# # pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2 #new_item keeps changing everytime ad the for loop item changes
#   b_list.append(new_item) #b_list is outside the for loop, so only one new item, which is the last change is added to it
#   print(b_list)

# mutate([1,2,3,5,8,13])
# --------My Solution-----------
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])


