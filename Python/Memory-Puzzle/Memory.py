import random
import time

# Create the board
def create_board():
    symbols = ['A','B','C','D','E','F','G','H']  # 8 pairs
    board = symbols * 2
    random.shuffle(board)
    return board

# Display the board with hidden cards
def display_board(board, revealed):
    print("\nBoard:")
    for i in range(len(board)):
        if revealed[i]:
            print(board[i], end=" ")
        else:
            print("*", end=" ")
        if (i + 1) % 4 == 0:
            print()
    print()

# Main game function
def play_game():
    board = create_board()
    revealed = [False] * 16
    attempts = 0

    while not all(revealed):
        display_board(board, revealed)
        try:
            first = int(input("Choose first card (0-15): "))
            second = int(input("Choose second card (0-15): "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if first == second or revealed[first] or revealed[second]:
            print("Invalid choices. Try again.")
            continue

        attempts += 1

        # Reveal chosen cards
        revealed[first] = True
        revealed[second] = True
        display_board(board, revealed)

        if board[first] != board[second]:
            print("Not a match!")
            time.sleep(1)
            revealed[first] = False
            revealed[second] = False
        else:
            print("Match found!")

    print(f"Congratulations! You completed the game in {attempts} attempts.")

if __name__ == "__main__":
    play_game()
