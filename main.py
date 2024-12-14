import GameState
import MonteCarloTreeSearch

# Main function
def main():
    game = TicTacToe()
    print("Welcome to Ultimate Tic Tac Toe!")
    while not game.is_terminal():
        if game.current_player == PLAYER_X:
            print("Your move! Enter board, row, col (e.g., 0 1 2):")
            action = tuple(map(int, input().split()))
            game.apply_action(action)
        else:
            print("AI is thinking...")
            root = Node(game.clone())
            best_move = monte_carlo_tree_search(root, iterations=1000)
            game.apply_action(best_move.state)
        # Print the global board
        for row in game.global_board:
            print(" ".join(row))
        print()

    winner = check_winner(game.global_board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()