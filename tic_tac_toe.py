import random
def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])
    print()
    print()

def win(board):
    if (board[0] == board[1] == board[2]):
        return (board[0]== 'x' or board[0] == 'o')
    if (board[3] == board[4] == board[5]):
        return (board[3] == 'x' or board[3] == 'o')
    if (board[6] == board[7] == board[8]):
        return (board[6] == 'x' or board[6] == 'o')
    if (board[0] == board[3] == board[6]):
        return (board[0][0] == 'x' or board[0] == 'o')
    if (board[1] == board[4] == board[7]):
        return (board[1] == 'x' or board[1] == 'o')
    if (board[2] == board[5] == board[8]):
        return (board[2] == 'x' or board[2] == 'o')
    if (board[0] == board[4] == board[8]):
        return (board[0] == 'x' or board[0] == 'o')
    if (board[2] == board[4] == board[6]):
        return (board[2] == 'x' or board[2] == 'o')
    return False

def move (board,player,position):
    board[position]= player
    return board

def position():
    print('Ingrese una posición donde desea colocar su pieza')
    position = int(input())
    return position

def autoposition(board):
    return random.choice(positionToChoose(board))

def positionToChoose(board):
    positionToChoose = []
    for index in range(len(board)):
        if (board[index] == ' '):
            positionToChoose.append(index)
    return positionToChoose

def choosePiece():
    print('Elija el tipo de pieza a utilizar para el jugador 1')
    player1 = input()
    return player1

def oposite(player1):
    if player1 == 'o' :
        return 'x'
    else:
        return 'o'

def play(player1,player2,round,board):
    state = 'Usted ha Empatado'
    for round in range(1,9):
        if (round % 2 == 0):
            board = move(board,player2,autoposition(board))
        else :
            board = move(board,player1,position())
        printBoard(board)
        if(win(board)):
            state = win_or_loose(round)
            break
    return state

def win_or_loose(result):
    if (result % 2 == 0):
        return 'Usted ha perdido'
    else:
        return 'Usted ha ganado'
def game():
    player1 = choosePiece()
    player2 = oposite(player1)
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    result = play(player1,player2,round,board)
    print(result)
game()