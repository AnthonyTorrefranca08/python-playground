import random
import sys
sys.setrecursionlimit(50)
#
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

# ROCK PAPER SCISSOR
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


# Head/Tails successful
Loop = True
while Loop:
    options = {
        0: "Heads",
        1: "Tails",
    }

    user_choice = input("Let's play a game if we choose the same you win, Heads or Tails? type q to quit\t").title()

    if user_choice in ["Head", "Hea", "He", "H"]:
        user_choice = "Heads"
    elif user_choice in ["Tail", "Tai", "Ta", "T"]:
        user_choice = "Tails"

    opponent = random.choice(list(options.values()))
    win_choice = random.choice(list(options.values()))

    if user_choice == "Q" or user_choice == "Quit":
        print("Thanks for playing!\n")
        Loop = False
    elif user_choice == "":
        print("Provide an answer!\n")
    elif user_choice not in list(options.values()):
        print("Please enter a valid answer! between Head or Tail\n")
    elif user_choice == opponent:
        if user_choice == win_choice:
            print(f"Your answer is {user_choice}, Bot's {opponent}, and the winning {win_choice}")
            print("It's a tie you both Won!\n")
        else:
            print(f"The winning choice is '{win_choice}'")
            print("No one won\n")
    elif opponent == win_choice:
        print(f"Your answer is {user_choice}, Bot's {opponent}, and the winning {win_choice}")
        print("The Opponent wins!\n")
    elif user_choice == win_choice:
        print(f"Your answer is {user_choice}, Bot's {opponent}, and the winning {win_choice}")
        print("You won!\n")
    else:
        print("That's not a valid answer!\n")

