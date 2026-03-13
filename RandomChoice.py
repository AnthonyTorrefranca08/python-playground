import random
from random import shuffle

# name = ["Angela", "Simon", "Jean", "Mary", "Angel"]
# names = random.choice(name)
#
# print(names)
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])
# # ROCK PAPER SCISSOR
# choices = {
#     0: "rock",
#     1: "paper",
#     2: "scissors",
# }
# beats = {
#     choices[0]: choices[2],
#     choices[1]: choices[0],
#     choices[2]: choices[1],
# }
# comp_choice = random.choice(choices)
# user_choice = input("Enter your choice: ").lower()
#
# print(user_choice)
# print(comp_choice)
#
# while user_choice == comp_choice:
#     print("It's a tie!")
#     user_choice = input("Enter your choice: ").lower()
#
# if beats[user_choice] < beats[comp_choice]:
#     print("You lose!")
#     user_choice = input("Enter your choice: ")
# else:
#     print("You win!")
#     user_choice = input("Enter your choice: ")
#
#
# Head/Tails successful
# import random
# Loop = True
# while Loop:
#     options = {
#         0: "Heads",
#         1: "Tails",
#     }
#
#     user_choice = input("Let's play a game if we choose the same you win, Heads or Tails? type q to quit\t").title()
#
#     if user_choice in ["Head", "Hea", "He", "H"]:
#         user_choice = "Heads"
#     elif user_choice in ["Tail", "Tai", "Ta", "T"]:
#         user_choice = "Tails"
#
#     opponent = random.choice(list(options.values()))
#     win_choice = random.choice(list(options.values()))
#
#     if user_choice == "Q" or user_choice == "Quit":
#         print("Thanks for playing!\n")
#         Loop = False
#     elif user_choice == "":
#         print("Provide an answer!\n")
#     elif user_choice not in list(options.values()):
#         print("Please enter a valid answer! between Head or Tail\n")
#     elif user_choice == opponent:
#         if user_choice == win_choice:
#             print(f"Your answer is {user_choice}, Bot's {opponent}, and the winning {win_choice}")
#             print("It's a tie you both Won!\n")
#         else:
#             print(f"The winning choice is '{win_choice}'")
#             print("No one won\n")
#     elif opponent == win_choice:
#         print(f"Your answer is {user_choice}, Bot's {opponent}, and the winning {win_choice}")
#         print("The Opponent wins!\n")
#     elif user_choice == win_choice:
#         print(f"Your answer is {user_choice}, Bot's {opponent}, and the winning {win_choice}")
#         print("You won!\n")
#     else:
#         print("That's not a valid answer!\n")
# student_scores = [99, 199, 249, 45, 69, 35, 59, 53, 452]
# highest_score = 0
#
# for highest in student_scores:
#     if highest >= highest_score:
#         highest_score = highest
#
# print(f'High score:  {highest_score}')


#
# total = 0
#
# for number in range(1, 101):
#     total += number
# print(total)
# total = 0
#
# for total in range(1, 101):
#     if total % 15 == 0:
#         print("FizzBuzz")
#     elif  total % 5 == 0:
#         print("Buzz")
#     elif total % 3 == 0:
#         print("Fizz")
#     else:
#         print(total)
#                                           NAH UH
#     useless piece of shutil
# import sys
# import random
#
# sys.setrecursionlimit(50)

# Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Symbols = [""" '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~'"""]
#
# # print(help(random))
#
# print("Welcome to Password Generator!")
#
# password_created = ""
#
# # user_letters = input("How many characters do you want in Letters(choose only 2 characters) ?")
# # user_symbols = input("How many characters do you want in Symbols(choose only 2 characters) ?")
# user_numbers = int(input("How many characters do you want in Numbers(choose only 2 characters)? "))
#
# line = 0
# i = 0
# num = ['1', '1', '1', '1']
# while line < user_numbers:
#     line += 1
#     i += 1
#     password = ""
#     print(f'Line {line}')
#     if line == user_numbers:
#         break
# sym_pref = int(input("Welcome, you are now in password generator. How many symbols do you want in ur password?\t"))
# num_pref = int(input("Welcome, you are now in password generator. How many numbers do you want in ur password?\t"))
# for letter in range(let_pref):
#     Letter = random.choice(Letters)
#     password = Letter
#
# for num in range(num_pref):
#     num = random.choice(Numbers)
#     password = num
#
# for sym in range(sym_pref):
#     sym = random.choice(Symbols)
#     password = sym
#
# print(f'{letter}, {num}, {sym}')

                                                  # Success!
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# symbols = [ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~']
#
# let_pref = int(input("Welcome, you are now in password generator. How many letters do you want in ur password?\t"))
# num_pref = int(input("Welcome, you are now in password generator. How many Numbers do you want in ur password?\t"))
# sym_pref = int(input("Welcome, you are now in password generator. How many Symbols do you want in ur password?\t"))
#
# password = ""
#
# for char in range (let_pref):
#     let_user_pref = random.choice(letters)
#     password += let_user_pref
# for char in range(num_pref):
#     num_user_pref = random.choice(numbers)
#     password += num_user_pref
# for sym in range(sym_pref):
#     symbol_user_pref = random.choice(symbols)
#     password += symbol_user_pref
#
# password_list = list(password)
# random.shuffle(password_list)
# password = "".join(password_list)
# print(password)


# ----------------------------------------------------------------------------------------------

# student_scores = {
#     "student 1": 73, "student 2": 95, "student 3": 60, "student 4": 88,
#     "student 5": 45, "student 6": 82, "student 7": 91, "student 8": 78
# }
#
# #
# # 'name' gets the key, 'score' gets the value
# for name, score in student_scores.items():
#     if score < 70:
#         print(f"Damn! {name} failed with a grade of {score}")

# 90 and above → "Outstanding"
# 80 to 89 → "Exceeds Expectations"
# 70 to 79 → "Acceptable"
# Below 70 → "Fail"

student_scores = {
    "student 1": 73, "student 2": 95, "student 3": 60, "student 4": 88,
    "student 5": 45, "student 6": 85, "student 7": 91, "student 8": 78
}

for name, grade in student_scores.items():
    if grade < 70:
        print(f"Damn! {name} failed the school with a grade of {grade}")
    elif 70 <= grade <= 79:
        print(f"Damn! {name} you slightly passed the school requirement with a grade of {grade}")
    elif 80 <= grade <= 89:
        print(f"Damn! {name} you exceeded our expectations with a grade of {grade}")
    elif 90 <= grade <= 99:
        print(f"Damn! {name} What an outstanding grade of {grade}")
    else:
        print(f" Bro, {name} Did you even study? your grade is this low {grade}")