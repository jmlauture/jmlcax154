# A simple program which pretends to play tic-tac-toe with the user
import random

def print_board(board):
    # Show the board grid
    print("+-------+-------+-------+")
    for row in board:
        #print(" ".join(row ))
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("+-------+-------+-------+")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def get_user_move(board):
    while True:
        try:
            move = input("Enter your move (row and column, e.g. '1 2'): ")
            row, col = map(int, move.split())
            if board[row][col] == " ":
                return row, col
            else:
                print("That cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers between 0 and 2.") 
def get_computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! \n-----------------------------")
    print()
    print("You are 'O' and the computer is 'X'.")
    print("===> 1st Row and 1st Column numbers are 0 (zero) <===")

    print()
    print_board(board)
    while True:
        # User's turn
        user_row, user_col = get_user_move(board)
        board[user_row][user_col] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("Congratulations! You win!")
            break
        # Computer's turn
        comp_row, comp_col = get_computer_move(board)
        board[comp_row][comp_col] = "X"
        print("Computer's move:")
        print_board(board)
        if check_winner(board, "X"):
            print("Computer wins! Better luck next time.")
            break     # Check for a draw
    else:
        print("It's a draw!")   
if __name__ == "__main__":    main()



