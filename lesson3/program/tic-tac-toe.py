# Create a new board.
def init_board():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Find the next player.
def next_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

# Print the board to the terminal.
def print_board(board):
    print("  0 1 2")
    for i in range(3):
        print(i, board[0][i], board[1][i], board[2][i])

# Check if the board has empty cell(s).
def has_empty(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return True
    
    return False

# Check if the game has ended.
# Returns (game ended, game winner)
def game_winner(board):
    # Assign shorter alias to variable.
    b = board

    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != ' ':
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != ' ':
            return b[0][i]
    
    if b[0][0] == b[1][1] == b[2][2] != ' ':
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != ' ':
        return b[0][2]
    
    return ' '
    
# A function to execute a player's action on the board.
def do_action(board, player, action):
    # Retrieve x and y coordinates of action.
    x, y = map(int, action)

    # Check that the grid is not filled.
    if board[x][y] != ' ':
        return False
    
    # Set the grid to filled.
    board[x][y] = player

    return True

def game():
    # Initialize the variables.
    board = init_board()
    win = False
    end = False
    player = 'O'
    winner = ' '

    # List of valid moves.
    valid_moves = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]

    while True:
        # Show a blank line for style.
        print()

        # Print the game board for player to see.
        print_board(board)
        # Show the current player.
        print("Current player:", player)
        # Receive input from user.
        action = input("Please enter XY of box: ")

        # Check that the move is one of the valid moves.
        if action not in valid_moves:
            print("Please enter a valid move!")
            continue
        
        # Execute user's action and check the action is valid.
        valid = do_action(board, player, action)
        # Show error if user's action is not valid.
        if not valid:
            print("Please enter a valid move!")
            continue
        
        # Update and check the game state.
        player = next_player(player)
        winner = game_winner(board)
        end = winner != ' '

        # Break the game loop if the game has ended.
        if end:
            break
    
    # Print board before the game ends.
    print_board(board)

    # Show the result to the player.
    if winner == ' ':
        print("It's a tie!")
    else:
        print("Player", winner, "has won!")

if __name__ == "__main__":
    game()