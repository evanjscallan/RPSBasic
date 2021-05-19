#ROCK PAPER SCISSORS - GAME
#DESIGNED BY EVAN SCALLAN, 2021

#Rules:
#Rock beats scissors
#scissors beats paper
#paper beats rock

#Random generator import
import random

#User and Opponent (Boss) Objects
boss = ['Rock', 'Paper', 'Scissors']
random_index = random.randint(0, len(boss)-1)
boss_choice =  boss[random_index]

#User Choice/Prompt
print("Rock,Paper, Scissors!""\nMake your choice:")
user_choice = input()

#Win, Lose, and Draw Variables
win = ("\033[1;33;1mYou Win!")
lose = ("\033[1;31;1mYou Lose")
draw = ("\033[1;32;1mIt's a Draw.")

#Opponent Choice
print("\033[1;32;1mOpponent's Choice:")
print("\033[1;35;1m" + boss_choice)

if user_choice == "Rock":
    if boss_choice == "Scissors":
        print(win)
    elif boss_choice == "Paper":
        print(lose)
    else:
        print(draw)

if user_choice == "Paper":
    if boss_choice == "Rock":
        print(win)
    elif boss_choice == "Scissors":
        print(lose)
    else:
        print(draw)

if user_choice == "Scissors":
    if boss_choice == "Paper":
        print(win)
    elif boss_choice == "Rock":
        print(lose)
    else:
        print(draw)


#END OF GAME - Thanks For Playing!




