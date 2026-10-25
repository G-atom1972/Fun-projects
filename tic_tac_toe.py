import math

# Create an empty board
board = [" " for _ in range(9)]


def print_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i + 3]))
        if i < 6:
            print("---+---+---")
    print()


def check_winner(b):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b1, c in winning_combinations:
        if b[a] != " " and b[a] == b[b1] == b[c]:
            return b[a]

    return None


def minimax(b, is_maximizing):
    winner = check_winner(b)

    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif " " not in b:
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = " "
                best_score = min(score, best_score)

        return best_score


def suggest_human_moves():
    """Analyzes the board and displays outcomes using the 3x3 visual format."""
    print("\n--- MOVE ANALYSIS FOR YOU (X) ---")
    
    best_score = math.inf
    analysis_board = []
    optimal_moves = []
    
    # Evaluate every spot on the grid
    for i in range(9):
        if board[i] != " ":
            # Keep original occupied marks visible in the suggestion grid
            analysis_board.append(board[i])
        else:
            board[i] = "X"
            score = minimax(board, True) 
            board[i] = " "
            
            if score == -1:
                analysis_board.append("WIN")
            elif score == 0:
                analysis_board.append("DRW")
            else:
                analysis_board.append("LOS")
                
            if score < best_score:
                best_score = score

    # Find which positions match the absolute best calculated score
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, True)
            board[i] = " "
            if score == best_score:
                optimal_moves.append(str(i + 1))

    # Print the 3x3 layout representation for outcomes
    for i in range(0, 9, 3):
        row = [f"{val:^3}" for val in analysis_board[i:i + 3]]
        print(" " + " | ".join(row))
        if i < 6:
            print("-----+-----+-----")
            
    print(f"\nMost optimal move(s): {', '.join(optimal_moves)}")
    print("---------------------------------")


def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"
    print("Computer chooses position:", best_move + 1)


def play_game():
    print("TIC-TAC-TOE USING MINIMAX")
    print("You are X | Computer is O")
    print("Choose positions from 1 to 9:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:
        print_board()
        
        # Display the visual board analysis map
        suggest_human_moves()

        # Human move
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue

        except ValueError:
            print("Enter a valid number.")
            continue

        board[move] = "X"

        if check_winner(board) == "X":
            print_board()
            print("Congratulations! You win!")
            break

        if " " not in board:
            print_board()
            print("It's a draw!")
            break

        # Computer move using Minimax
        computer_move()

        if check_winner(board) == "O":
            print_board()
            print("Computer wins!")
            break

        if " " not in board:
            print_board()
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
