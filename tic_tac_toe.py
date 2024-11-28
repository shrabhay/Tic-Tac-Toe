import os
os.system('clear')

GAME_ON = True
X_SCORE = 0
O_SCORE = 0
CURRENT_PLAYER = 'X'


def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("_________")


def make_move(player, board):
    move_is_correct = False
    while not move_is_correct:
        move = int(input(f"Player {player}, enter your move (1 - 9): "))
        if 1 <= move <= 9:
            move_is_correct = True

            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] != ' ':
                print("The selected position is already filled, try again...")
                move_is_correct = False
            else:
                board[row][col] = player

        else:
            print("Invalid input, try again...")


def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)


def is_winner(player, board):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True

        if all(board[j][i] == player for j in range(3)):
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def play_game():
    global GAME_ON, X_SCORE, O_SCORE, CURRENT_PLAYER

    current_board = [[' ' for _ in range(3)] for _ in range(3)]

    while GAME_ON:
        os.system('clear')
        print_board(board=current_board)
        make_move(player=CURRENT_PLAYER, board=current_board)

        if is_winner(player=CURRENT_PLAYER, board=current_board):
            print_board(board=current_board)
            if CURRENT_PLAYER == 'X':
                X_SCORE += 1
            else:
                O_SCORE += 1
            print(f"Player {CURRENT_PLAYER} wins this round!!!")
            print(f"X - {X_SCORE} WINS\nO - {O_SCORE} WINS")
            break
        elif is_board_full(board=current_board):
            print_board(board=current_board)
            print("It's a TIE!!")
            print(f"X - {X_SCORE} WINS\nO - {O_SCORE} WINS")
            break
        else:
            CURRENT_PLAYER = 'O' if CURRENT_PLAYER == 'X' else 'X'


while True:
    user_game_on = input("Would you like to play a game of TIC TAC TOE? Enter 'Y' or 'N': ").lower()
    if user_game_on == 'y':
        play_game()
        CURRENT_PLAYER = 'O' if CURRENT_PLAYER == 'X' else 'X'
    else:
        print(f"Final Score:\nX - {X_SCORE}\nO - {O_SCORE}")
        if X_SCORE != O_SCORE:
            final_winner = 'X' if X_SCORE > O_SCORE else 'Y'
            print(f"PLAYER {final_winner} WINS THE GAME!!!")
        else:
            print("THE GAME TIED!!")
        break
