import random

print("Welcome to Tic-Tac-Toe! \n-----------------------------")
print("You are 'O' and the computer is 'X'.")

def display_board(board):
    """Prints the current state of the board to the console."""
    print("\nCurrent board:")

    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    """Asks the user for their move, validates it, and updates the board."""
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid number! Please pick a number between 1 and 9.")
                continue
            
            # Convert the 1-9 number into 0-indexed row and column coordinates
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            # Check if the chosen square is occupied
            if board[row][col] in ['X', 'O']:
                print("That square is already occupied! Try another one.")
                continue
                
            # If valid, assign the user's mark 'O'
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def make_list_of_free_fields(board):
    """Returns a list of tuples containing (row, col) for all empty squares."""
    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free_fields.append((r, c))
    return free_fields


def check_victory_for(board, sign):
    """Checks if the player with the given 'sign' ('X' or 'O') has won."""
    # Check Rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == sign:
            return True
            
    # Check Columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == sign:
            return True
            
    # Check Diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
        
    return False


def draw_move(board):
    """Makes a random move for the computer ('X') from available free fields."""
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'


# =====================================================================
# MAIN GAME LOOP
# =====================================================================
if __name__ == "__main__":
    # Initialize the board with numbers 1-9 as strings
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    
    # Assumption: Computer always makes the first move right in the middle (Square 5)
    board[1][1] = 'X'
    print("The computer has made its first move.")
    
    while True:
        display_board(board)
        
        # 1. User's Turn
        enter_move(board)
        if check_victory_for(board, 'O'):
            display_board(board)
            print("You win!")
            break
            
        # Check for a tie after user move
        if not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break
            
        # 2. Computer's Turn
        print("\nComputer is making its move...")
        draw_move(board)
        if check_victory_for(board, 'X'):
            display_board(board)
            print("The computer wins!")
            break
            
        # Check for a tie after computer move
        if not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break