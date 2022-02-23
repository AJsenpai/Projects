import os
import time
import random
def display_board(board):
    
    print('     |      |    ')
    print('  ' + board[7] + '  |  '+ board[8]+'   |  '+board[9] )
    print('     |      |    ')
    print(' -------------------')
    print('     |      |    ')
    print('  ' + board[4] + '  |  '+ board[5]+'   |  '+board[6] )
    print('     |      |    ')
    print(' -------------------')
    print('     |      |    ')
    print('  ' + board[1] + '  |  '+ board[2]+'   |  '+board[3] )
    print('     |      |    ')
    
    
    
    # time.sleep(1)
    # os.system('clear')
    

def choose_first():
    if bool(random.getrandbits(1)) == True :
        print("Player 1 will go first\n")
        player='P1'
    else:
        print("Player 2 will go first\n")
        player='P2'
    return player


    
def playerinputkey():
        player_key=input('choose your key [ X ] or [ O ] ').upper()
        if player_key not in ['X','O']:
            print("invalid choice try again")
            playerinputkey()
        if player_key == 'X':
            player1='X'
            player2='O'
        else:
            player1='O'
            player2='X'
            
        return [player1,player2]
 
    
def iswinner(b,k):
    return ( (b[1]==k and b[2]==k and b[3]==k) or
           (b[4]==k and b[5]==k and b[6]==k) or
           (b[7]==k and b[8]==k and b[9]==k) or
           (b[7]==k and b[8]==k and b[9]==k) or
           (b[1]==k and b[4]==k and b[7]==k) or
           (b[2]==k and b[5]==k and b[8]==k) or
           (b[3]==k and b[6]==k and b[9]==k) or
           (b[1]==k and b[5]==k and b[9]==k) or
           (b[3]==k and b[5]==k and b[7]==k) )


def isboardfull(board):
    if ' ' in board:
        return False
    else:
        return True

def isspacefree(board,move):
    while move  not in range(1,10):
        return False
    else:
        if board[move] in ' ':
            return True
        else:
            return False


def makemove(board,key,move):
    board[move]=key
    
    
def inputcheck(move):
    if move in range(1,10) and move!=None:
        return True
    else:
        return True
    
    
        
    

def main():
    while True:
        board=[' ']*10
        board[0]='#'
        time.sleep(1)
        os.system('clear')
        print('#####################################')
        print('#     Welcome to TIC TAC TOE Game   #')
        print('#####################################\n')
        player1,player2=playerinputkey()
        print("Player 1 = {}\nPlayer 2 = {} \n".format(player1,player2))
        turn=choose_first()
        time.sleep(1)
        gameplaying=True
    
        while gameplaying:
            if turn=='P1':
                    os.system('clear')
                    display_board(board)
                    move=int(input("make your move P1  "))
                    while not isspacefree(board,move):
                        print("Errr Occupied!!! Try Different Move...\n[Help]:Move should be in range 1-9 which is not occupied")
                        move=int(input("make your move P1  "))
                    else:
                        makemove(board,player1,move)
                        
                    if isboardfull(board):
                        os.system('clear')
                        display_board(board)
                        print("\n\nIt's a TIE.... \n -----Game-Over-----")
                        break
                    if iswinner(board,player1):
                        os.system('clear')
                        display_board(board)
                        print("\t\t\t\t\t\t---------- " + " PLAYER 2 " +"---------")
                        print("\t\t\t\t\t\t_____________" + " WON " + "_____________")
                        gameplaying=False
                        break
    
                    else:
                        turn='P2'
                    
            else:
                os.system('clear')
                display_board(board)
                move=int(input("make your move P2  "))
                # makemove(board,player2,move)
                while not isspacefree(board,move):
                    print("Errr Occupied!!! Try Different Move...\n[Help]:Move should be in range 1-9 which is not occupied")
                    move=int(input("make your move P2  "))
                else:
                    makemove(board,player2,move)
                
                if isboardfull(board):
                    os.system('clear')
                    display_board(board)
                    print("\n\nIt's a TIE.... \n -----Game-Over-----")
                    break
                if iswinner(board,player2):
                        os.system('clear')
                        display_board(board)
                        print("\t\t\t\t\t\t---------- " + " PLAYER 2 " +"---------")
                        print("\t\t\t\t\t\t_____________" + " WON " + "_____________")
                        gameplaying=False
                        break
                
                else:
                    turn='P1'
        again=input("\n Yo Want to Play again Y/N ?:  ")
        if again.upper()=='Y':
            main()
        else:
            break
                


main()        
    
    #board=['#','X','O','X','O','X','O','X','O','X']   
    
    # display_board(board)
    






    


        
        
    
