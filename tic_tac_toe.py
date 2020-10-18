def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

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

def move (board,player):
    print('Ingrese una posición donde desea colocar su pieza')
    position = int(input())
    board[position]= player
    return board

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
    while win(board) == False:
        round = round+1
        if (round % 2 == 0):
            board = move(board,player2)
        else :
            board = move(board,player1)
        printBoard(board)
def game():
    player1 = choosePiece()
    player2 = oposite(player1)
    round = 0
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    play(player1,player2,round,board)
    print('Usted ha ganado jugador')
game()