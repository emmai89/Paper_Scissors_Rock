import random
import os

os.system('cls||clear')
random.seed()

options = ['p', 's', 'r']

while True:
    botMove = options[random.randrange(0,3)]
    userMove = input("\n\np - paper \ns - scissors\nr - rock\nq - quit\n\nSelect: ")
    os.system('cls||clear')

    if userMove == botMove :
        print("it's a draw")
        print(userMove, botMove)

    elif (userMove == 'p' and botMove == 'r') or (userMove == 'r' and botMove == 's') or (userMove == 's' and botMove == 'p') :
        print(" You Win!!\n", userMove +" beats ", botMove)

    elif (userMove == 'q') :
        break

    else :
        print (" You Lose!!\n", botMove +" beats ", userMove)
