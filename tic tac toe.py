def draw_board(board):
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("-----------")
    print(f" {board[1]} | {board[2]} | {board[3]} ")

def get_move(player_letter):
    move = input(f"{player_letter}, enter your move (1-9): ")
    try:
        move = int(move)
        if move >= 1 and move <= 9:
            return move
        else:
            print("Invalid move, try again")
            return get_move(player_letter)
    except ValueError:
        print("Invalid input, try again")
        return get_move(player_letter)

def make_move(board, player_letter, move):
    board[move] = player_letter

def is_winner(board, player_letter):
    return (
        # rows
        (board[7] == player_letter and board[8] == player_letter and board[9] == player_letter)
        or (board[4] == player_letter and board[5] == player_letter and board[6] == player_letter)
        or (board[1] == player_letter and board[2] == player_letter and board[3] == player_letter)
        # columns
        or (board[7] == player_letter and board[4] == player_letter and board[1] == player_letter)
        or (board[8] == player_letter and board[5] == player_letter and board[2] == player_letter)
        or (board[9] == player_letter and board[6] == player_letter and board[3] == player_letter)
        # diagonals
        or (board[7] == player_letter and board[5] == player_letter and board[3] == player_letter)
        or (board[9] == player_letter and board[5] == player_letter and board[1] == player_letter)
    )

def is_board_full(board):
    for i in range(1,10):
        if board[i] == " ":
            return False
    return True

board = [" "] * 10
current_player = "X"

while True:
    draw_board(board)
    move = get_move(current_player)
    make_move(board, current_player, move)
    if is_winner(board, current_player):
        draw_board(board)
        print(f"{current_player} wins!")
        break
    if is_board_full(board):
        draw_board(board)
        print("It's a tie!")
        break
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"