import os
import time
import random
import sys


def display_board(board):
    print("#####################################")
    print("#     Welcome to TIC TAC TOE Game   #")
    print("#####################################\n")

    print("\t", "     |      |    ")
    print("\t", "  " + board[7] + "  |  " + board[8] + "   |  " + board[9])
    print("\t", "     |      |    ")
    print("\t", "-------------------")
    print("\t", "     |      |    ")
    print("\t", "  " + board[4] + "  |  " + board[5] + "   |  " + board[6])
    print("\t", "     |      |    ")
    print("\t", "--------------------")
    print("\t", "     |      |    ")
    print("\t", "  " + board[1] + "  |  " + board[2] + "   |  " + board[3])
    print("\t", "     |      |    ")
    print()

    # time.sleep(1)
    # os.system('clear')


def isspacefree(board, move):
    return board[move] == " "


def iswinner(b, k):  # b=board, key=letter
    return (
        (b[1] == k and b[2] == k and b[3] == k)
        or (b[4] == k and b[5] == k and b[6] == k)
        or (b[7] == k and b[8] == k and b[9] == k)
        or (b[7] == k and b[8] == k and b[9] == k)
        or (b[1] == k and b[4] == k and b[7] == k)
        or (b[2] == k and b[5] == k and b[8] == k)
        or (b[3] == k and b[6] == k and b[9] == k)
        or (b[1] == k and b[5] == k and b[9] == k)
        or (b[3] == k and b[5] == k and b[7] == k)
    )


def playerMove(board, key):
    while True:
        try:
            pos = int(input(f"make your move player {key.upper()}\t"))
            if pos in range(1, 10) and pos != None:
                if isspacefree(board, pos):
                    makemove(board, key, pos)
                    break
                else:
                    print("position occupied")
            else:
                print("move range is 1-9")
        except:
            print("invalid Input! move range is 1-9")


def compMove(board, key):
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0
    for letter in ["O", "X"]:
        for i in possible_moves:
            boardcopy = board[:]
            boardcopy[i] = letter
            if iswinner(boardcopy, letter):
                move = i
                return move

    # first priority to corners
    open_corners = []
    for i in possible_moves:
        if i in (1, 3, 7, 9):
            open_corners.append(i)
    if open_corners:
        move = selectRandom(open_corners)
        return move

    # second priority to center
    if 5 in possible_moves:
        return 5

    # third priority to center
    open_edges = []
    for i in possible_moves:
        if i in (2, 4, 6, 8):
            open_edges.append(i)

    if open_edges:
        move = selectRandom(open_edges)
    return move


def selectRandom(possible_moves):
    return random.choice(possible_moves)


def isboardfull(board):
    if board.count(" ") == 0:
        return True
    else:
        return False
    # print(bool(board.count(" ") < 1))
    # return board.count(" ") == 0


def playerinputkey():
    player_key = input("choose your key [ X ] or [ O ] ").upper()
    if player_key not in ["X", "O"]:
        print("invalid choice try again")
        playerinputkey()
    if player_key == "X":
        player1 = "X"
        player2 = "O"
    else:
        player1 = "O"
        player2 = "X"

    return player1, player2


def makemove(board, key, pos):
    board[pos] = key


# def choose_first():
#     if bool(random.getrandbits(1)) == True :
#         print("Player 1 will go first\n")
#         player='P1'
#     else:
#         print("Player 2 will go first\n")
#         player='P2'
#     return player


def play_game(board, computer):
    player1, player2 = playerinputkey()
    players = {player1: "Player1", player2: "Player2"}
    print("Player 1 = {}\nPlayer 2 = {} \n".format(player1, player2))
    # turn = choose_first()
    # time.sleep(1)
    while not (isboardfull(board)):
        if not (iswinner(board, player2)):
            playerMove(board, player1)
            os.system("cls")
            display_board(board)
        else:
            print(f"{players[player2]} [{player2}] Won the Game!")
            break

        if not (iswinner(board, player1)):
            if computer:
                move = compMove(board, player2)
                if move == 0:  # if move is zero
                    # print("TIE Game 1")
                    break
                else:
                    makemove(board, player2, move)
                    os.system("cls")
                    display_board(board)
            else:
                playerMove(board, player2)
                os.system("cls")
                display_board(board)
        else:
            print(f"{players[player1]} [{player1}] Won the Game!")
            break

    if isboardfull(board):
        print("Tie Game ")


def start():
    while True:
        board = [" "] * 10
        board[0] = "#"
        os.system("cls")
        # print("#####################################")
        # print("#     Welcome to TIC TAC TOE Game   #")
        # print("#####################################\n")
        display_board(board)
        print("Choose Options:\n")
        try:
            option = int(input("1. Two Players\n2. With Computer\n3. Exit\n"))
            if option < 1 or option > 3:
                print("Invalid Option! Available Options 1-3")
            elif option == 3:
                # sys.exit()
                break
            else:
                computer = True if option == 2 else False
                play_game(board, computer)
                # break
        except:
            print("invalid input")
            # start()
        play_again = input("\nYo Want to Play again Y/N ?:  ")
        if play_again.upper() == "Y":
            start()
        else:
            sys.exit()


start()

# board=['#','X','O','X','O','X','O','X','O','X']

