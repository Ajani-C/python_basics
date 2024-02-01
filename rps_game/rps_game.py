# TO DO:
""" Modify this program to include a menu
    and use number to designate the user_input
1 - Rock
2 - Paper
3 - Scissors
"""
# Rock, Paper, Scissors Game against computer

# import random function
import random


def main():
    again = input("Do you want to play 'Rock-Paper-Scissors'? Or enter n to quit: ").lower()
    while again != 'n':
        computer_randomized_choice()
        user_choice()
        again = input("Do you want to play 'Rock-Paper-Scissors': y/n  ")
    print("Good Bye")
    quit()


def computer_randomized_choice():
    """ get computer choice game_choice = ['rock', 'paper', 'scissors']"""
    global computer_choice
    computer_choice = random.randint(1, 3)
    print("The computer played")
    return computer_choice


# get user choice
def user_choice():
    user_input = input("Enter your choice: 1 for Rock, 2 for Paper, 3 for Scissors: ")
    print('user_input:', user_input)
    if user_input == "1":  # Rock
        user_choice_rock()
    elif user_input == "2":  # Paper
        user_choice_paper()
    elif user_input == "3":  # Scissors
        user_choice_scissors()
    else:
        user_choice()
    print("//////////////////////////////////////////////////////////")
    main()


# compare user choice and computer choice
def user_choice_rock():  # user selected 1 or rock
    if computer_choice == 1:
        print("YOU TIE: you entered 'Rock' and Computer selected 'Rock'")
    elif computer_choice == 2:
        print("YOU LOSE: you entered 'Rock' and Computer selected 'Paper'")
    elif computer_choice == 3:
        print("YOU WIN: you entered 'Rock' and Computer selected 'Scissors'")
    else:
        print("Try Again")
        user_choice()


def user_choice_paper():  # user selected 2 or paper
    if computer_choice == 1: # computer selected rock
        print("YOU WIN: you entered 'Paper' and Computer selected 'Rock'")
    elif computer_choice == 2: # computer selected paper
        print("YOU TIE: you entered 'Paper' and Computer selected 'Paper'")
    elif computer_choice == 3: # computer selected scissors
        print("YOU LOSE: you entered 'Paper' and Computer selected 'Scissors'")
    else:
        print("Try Again")
        user_choice()


def user_choice_scissors():  # user selected 3 or scissors
    if computer_choice == 1: # computer selected rock
        print("YOU LOSE: you entered 'Scissors' and Computer selected 'Rock'")
    elif computer_choice == 2: # computer selected paper
        print("YOU WIN: you entered 'Scissors' and Computer selected 'Paper'")
    elif computer_choice == 3: # computer selected scissors
        print("YOU TIE: you entered 'Scissors' and Computer selected 'Scissors'")
    else:
        print("Try Again")
        user_choice()


main()



#Ajani Cole
