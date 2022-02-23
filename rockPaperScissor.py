import sys, random, os, time

# Date: Feb,18 2020
# Author: Ajay
# Desciption: Simple Stone Paper Scissor Game in pyton3
# Date Modified: Feb,18 2020

# keep track of number of wins,tie and looses
wins = 0
looses = 0
tie = 0

# Main Game Loops
pmapping = {"r": "ROCK", "p": "PAPER", "s": "SCISSOR"}
cmapping = {1: "ROCK", 2: "PAPER", 3: "SCISSOR"}

while True:
    print("_____________ ROCK PAPER SCISSOR _______________\n")
    print("WINS {} | LOOSES {} | TIE {} \n".format(wins, looses, tie))
    while True:
        # print("Rock? Paper? Scissor?")
        player_move = input("Rock(r)? Paper(p)? Scissor(s) QUIT(q)? ")
        if player_move.lower() == "q":
            sys.exit()
        if player_move.lower() in ("r", "p", "s"):
            break

        print("Valid input values are (r,p,s,q)")

    computer_move = random.randint(1, 3)

    if player_move in ("r", "p", "s"):
        print(
            "{} VERSUS {}".format(
                pmapping.get(player_move), cmapping.get(computer_move)
            )
        )

    if pmapping.get(player_move) == cmapping.get(computer_move):
        tie += 1
    if player_move.lower() == "r" and computer_move == 3:
        wins += 1
    if player_move.lower() == "r" and computer_move == 2:
        looses += 1
    if player_move.lower() == "p" and computer_move == 3:
        looses += 1
    if player_move.lower() == "p" and computer_move == 1:
        wins += 1
    if player_move.lower() == "s" and computer_move == 1:
        looses += 1
    if player_move.lower() == "s" and computer_move == 2:
        wins += 1

    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

