def printBoard(board):
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('-+-+-')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('-+-+-')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])

def win(board):
    if (board[0][0] == board[0][1] == board[0][2]):
        return (board[0][0] == 'x' or board[0][0] == 'o')
    if (board[1][0] == board[1][1] == board[1][2]):
        return (board[1][0] == 'x' or board[1][0] == 'o')
    if (board[2][0] == board[2][1] == board[2][2]):
        return (board[2][0] == 'x' or board[2][0] == 'o')
    if (board[0][0] == board[1][0] == board[2][0]):
        return (board[0][0] == 'x' or board[0][0] == 'o')
    if (board[0][1] == board[1][1] == board[2][1]):
        return (board[0][1] == 'x' or board[0][1] == 'o')
    if (board[0][2] == board[1][2] == board[2][2]):
        return (board[0][2] == 'x' or board[0][2] == 'o')
    if (board[0][0] == board[1][1] == board[2][2]):
        return (board[0][0] == 'x' or board[0][0] == 'o')
    if (board[0][2] == board[1][1] == board[2][0]):
        return (board[0][2] == 'x' or board[0][2] == 'o')
    return False

def move (board,player):
    print('Ingrese una columna donde desea colocar su pieza')
    column = int(input())
    print('Ingrese una fila donde desea colocar su pieza')
    row = int(input())
    board[column][row] = player
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
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    play(player1,player2,round,board)
    print('Usted ha ganado jugador')
game()