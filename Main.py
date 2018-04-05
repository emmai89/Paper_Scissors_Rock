import random
import os

os.system('cls||clear')
random.seed()

options = ['p', 's', 'r']
scores = [0, 0]

while True:
    botMove = options[random.randrange(0,3)]
    userMove = input("\n\np - paper \ns - scissors\nr - rock\nq - quit\n\nSelect: ")
    os.system('cls||clear')


    if userMove == botMove :
        print(" It's a Draw")
        print("", userMove, "and", botMove, "are the same")

    elif (userMove == 'p' and botMove == 'r') or (userMove == 'r' and botMove == 's') or (userMove == 's' and botMove == 'p') :
        print(" You Win!!\n", userMove +" beats ", botMove)
        scores[0] += 1

    elif (userMove == 'q') :
        break

    else :
        print (" You Lose!!\n", botMove +" beats ", userMove)
        scores[1] += 1

    print(" Scores: user ", scores[0], "bot ", scores[1])
