import random
import math

# Constants
PLAYER_X = "X"  # Human player
PLAYER_O = "O"  # AI player
EMPTY = "."     # Empty cell

# Helper function: Check if a board is a win
def check_winner(board):
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    # No winner yet
    return None

# Helper function: Check if a board is full
def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Tic Tac Toe game logic
class TicTacToe:
    def __init__(self):
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = PLAYER_X

    def get_legal_actions(self):
        # Return a list of all empty cells as legal moves
        return [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == EMPTY]

    def apply_action(self, action):
        row, col = action
        if self.board[row][col] != EMPTY:
            raise ValueError("Illegal move!")
        self.board[row][col] = self.current_player
        # Switch players
        self.current_player = PLAYER_X if self.current_player == PLAYER_O else PLAYER_O

    def is_terminal(self):
        # The game is over if there is a winner or the board is full
        return check_winner(self.board) is not None or is_full(self.board)

    def get_reward(self):
        # AI (O) wins: +1, Human (X) wins: -1, Draw: 0
        winner = check_winner(self.board)
        if winner == PLAYER_O:
            return 1
        elif winner == PLAYER_X:
            return -1
        return 0

    def clone(self):
        # Create a deep copy of the game state
        clone = TicTacToe()
        clone.board = [row[:] for row in self.board]
        clone.current_player = self.current_player
        return clone
