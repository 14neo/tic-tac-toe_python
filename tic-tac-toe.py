board = [["_","_","_"],["_","_","_"],["_","_","_"]]

def display_board(board):
    for row in board:
        print(" ".join(row))


def if_full_board(board):
    cnt = 0
    for row in board:
        cnt += row.count("_")

    if cnt == 0:
        return True
    else:
        return False


def is_valid_move(row, col):
    if row >=3 or col >= 3 or  row < 0 or col < 0:
        return False
    else:
        return True


def row_filled(board, symbol):
    for row in board:
        if row.count(symbol) == 3:
            return True
    return False


def col_filled(board, symbol):
    if board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol:
        return True
    elif board[0][1] == symbol and board[1][1] == symbol and board [2][1] == symbol:
        return True
    elif board [0][2] == symbol and board[1][2] == symbol and board [2][2] == symbol:
        return True
    else:
        return False


def diagonal_filled(board, symbol):
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    elif board[0][2] == symbol and board[1][1] ==symbol and board[2][0] == symbol:
        return True
    else:
        return False
     

# game start
display_board(board)

player1 = input("Player 1 (X), please enter your name: ")
player2 = input("Player 2 (O), please enter your name: ")

current_player = player1

while True:
    move = input(f"{current_player}, please enter your move: eg. row,col: ")
    row, col = move.split(",")
    row, col = int(row), int(col)

    # check if move is valid
    if not is_valid_move(row, col):
        print("Invalid move, try again")
        continue

    if board[row][col] == "_":
        if current_player == player1:
            board[row][col] = "X"
        else:
            board[row][col] = "O"
    else:
        print("Invalid move, try again")
        continue

    # check if current player wins
    if current_player == player1:
        symbol = "X"
    else:
        symbol = "O"

    # check row
    if row_filled(board, symbol):
        display_board(board)
        print(f"{current_player} wins")
        break

    # check col
    if col_filled(board, symbol):
        display_board(board)
        print(f"{current_player} wins")
        break

    # check diagonal
    if diagonal_filled(board, symbol):
        display_board(board)
        print(f"{current_player} wins")
        break
    
    
    # change player for next move
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

    display_board(board)
    print()

    if if_full_board(board):
        print("Game Drawn")
        break


