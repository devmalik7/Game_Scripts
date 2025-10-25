"""
Dots and Boxes - Command Line Implementation

A classic two-player game where players take turns connecting dots to form boxes.
The player who completes more boxes wins the game.

Author: AI Assistant (fixed)
Date: 2024 (updated)
"""

import os
import sys


class DotsAndBoxes:
    def __init__(self, rows=3, cols=3):
        """
        Initialize the game board.

        Args:
            rows (int): Number of rows of boxes
            cols (int): Number of columns of boxes
        """
        self.rows = rows
        self.cols = cols
        # Grid dimensions: (2*rows + 1) x (2*cols + 1)
        self.grid = [[' ' for _ in range(2 * cols + 1)] for _ in range(2 * rows + 1)]
        self.scores = {'A': 0, 'B': 0}
        self.current_player = 'A'
        self.game_over = False

        # Initialize dots
        for i in range(0, 2 * rows + 1, 2):
            for j in range(0, 2 * cols + 1, 2):
                self.grid[i][j] = '•'

        # Track completed boxes and drawn lines
        # horizontal_lines: (rows + 1) x cols  -> between horizontally adjacent dots
        # vertical_lines: rows x (cols + 1)    -> between vertically adjacent dots
        self.completed_boxes = [[False for _ in range(cols)] for _ in range(rows)]
        self.horizontal_lines = [[False for _ in range(cols)] for _ in range(rows + 1)]
        self.vertical_lines = [[False for _ in range(cols + 1)] for _ in range(rows)]

    def display_board(self):
        """Display the current state of the game board."""
        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "=" * 50)
        print("          DOTS AND BOXES")
        print("=" * 50)
        print(f"Player A: {self.scores['A']} points")
        print(f"Player B: {self.scores['B']} points")
        print(f"Current Player: {self.current_player}")
        print("=" * 50)

        for i in range(len(self.grid)):
            row_display = ""
            for j in range(len(self.grid[i])):
                # Handle dots, lines, and box contents
                if i % 2 == 0 and j % 2 == 0:  # Dot positions
                    row_display += self.grid[i][j]
                elif i % 2 == 0:  # Horizontal positions
                    # Stored as '-' when drawn
                    if self.grid[i][j] == '-':
                        row_display += '─'
                    else:
                        row_display += ' '
                elif j % 2 == 0:  # Vertical positions
                    if self.grid[i][j] == '|':
                        row_display += '│'
                    else:
                        row_display += ' '
                else:  # Box centers
                    if self.grid[i][j] in ['A', 'B']:
                        row_display += self.grid[i][j]
                    else:
                        row_display += ' '

                # Add spacing between elements
                if j % 2 == 0 and j < len(self.grid[i]) - 1:
                    row_display += ' '
            print(row_display)

        print("=" * 50)

    def is_valid_move(self, row1, col1, row2, col2):
        """
        Check if a move is valid.

        Args:
            row1, col1: Coordinates of first dot (0-based, dot coordinates)
            row2, col2: Coordinates of second dot

        Returns:
            bool: True if move is valid, False otherwise
        """
        # Ensure coordinates are integers and within dot indices
        if not all(isinstance(x, int) for x in (row1, col1, row2, col2)):
            return False

        if not (0 <= row1 <= self.rows and 0 <= col1 <= self.cols and
                0 <= row2 <= self.rows and 0 <= col2 <= self.cols):
            return False

        # Convert to grid coordinates
        grid_row1, grid_col1 = row1 * 2, col1 * 2
        grid_row2, grid_col2 = row2 * 2, col2 * 2

        # Check if connecting adjacent dots (Manhattan distance = 2 in grid coords)
        if abs(grid_row1 - grid_row2) + abs(grid_col1 - grid_col2) != 2:
            return False

        # Check if line is already drawn
        if grid_row1 == grid_row2:  # Horizontal line
            line_col = min(grid_col1, grid_col2) // 2
            line_row = grid_row1 // 2
            if self.horizontal_lines[line_row][line_col]:
                return False
        else:  # Vertical line
            line_row = min(grid_row1, grid_row2) // 2
            line_col = grid_col1 // 2
            if self.vertical_lines[line_row][line_col]:
                return False

        return True

    def draw_line(self, row1, col1, row2, col2):
        """
        Draw a line between two dots and check for completed boxes.

        Args:
            row1, col1: Coordinates of first dot
            row2, col2: Coordinates of second dot

        Returns:
            bool: True if a box was completed (player gets another turn), False otherwise
        """
        grid_row1, grid_col1 = row1 * 2, col1 * 2
        grid_row2, grid_col2 = row2 * 2, col2 * 2

        box_completed = False

        if grid_row1 == grid_row2:  # Horizontal line
            line_col = min(grid_col1, grid_col2) // 2
            line_row = grid_row1 // 2
            self.horizontal_lines[line_row][line_col] = True

            # Update grid display (place '-' in the middle)
            mid_col = (grid_col1 + grid_col2) // 2
            self.grid[grid_row1][mid_col] = '-'

            # Check for boxes above and below
            if line_row > 0:  # Check box above
                if (self.horizontal_lines[line_row - 1][line_col] and
                        self.vertical_lines[line_row - 1][line_col] and
                        self.vertical_lines[line_row - 1][line_col + 1]):
                    self.complete_box(line_row - 1, line_col)
                    box_completed = True

            if line_row < self.rows:  # Check box below
                if (self.horizontal_lines[line_row + 1][line_col] and
                        self.vertical_lines[line_row][line_col] and
                        self.vertical_lines[line_row][line_col + 1]):
                    self.complete_box(line_row, line_col)
                    box_completed = True

        else:  # Vertical line
            line_row = min(grid_row1, grid_row2) // 2
            line_col = grid_col1 // 2
            self.vertical_lines[line_row][line_col] = True

            # Update grid display (place '|' in the middle)
            mid_row = (grid_row1 + grid_row2) // 2
            self.grid[mid_row][grid_col1] = '|'

            # Check for boxes left and right
            if line_col > 0:  # Check box to the left
                if (self.vertical_lines[line_row][line_col - 1] and
                        self.horizontal_lines[line_row][line_col - 1] and
                        self.horizontal_lines[line_row + 1][line_col - 1]):
                    self.complete_box(line_row, line_col - 1)
                    box_completed = True

            if line_col < self.cols:  # Check box to the right
                if (self.vertical_lines[line_row][line_col + 1] and
                        self.horizontal_lines[line_row][line_col] and
                        self.horizontal_lines[line_row + 1][line_col]):
                    self.complete_box(line_row, line_col)
                    box_completed = True

        return box_completed

    def complete_box(self, box_row, box_col):
        """
        Mark a box as completed for the current player.

        Args:
            box_row: Row index of the box
            box_col: Column index of the box
        """
        if not self.completed_boxes[box_row][box_col]:
            self.completed_boxes[box_row][box_col] = True
            self.scores[self.current_player] += 1

            # Mark the box with player's initial
            center_row = box_row * 2 + 1
            center_col = box_col * 2 + 1
            self.grid[center_row][center_col] = self.current_player

    def check_game_over(self):
        """Check if all boxes have been completed."""
        return all(all(row) for row in self.completed_boxes)

    def switch_player(self):
        """Switch to the other player."""
        self.current_player = 'B' if self.current_player == 'A' else 'A'

    def get_winner(self):
        """Determine the winner based on scores."""
        if self.scores['A'] > self.scores['B']:
            return 'A'
        elif self.scores['B'] > self.scores['A']:
            return 'B'
        else:
            return 'Tie'

    def play_turn(self):
        """Handle a single player's turn."""
        while True:
            try:
                print("\nEnter coordinates for your line (format: row1 col1 row2 col2)")
                print(f"Rows and columns are 0-based dots: row in [0..{self.rows}], col in [0..{self.cols}]")
                print("Example: '0 0 0 1' to connect dot at (0,0) to (0,1)")
                coords = input("Your move: ").strip().split()

                if len(coords) != 4:
                    print("Please enter exactly 4 numbers separated by spaces.")
                    continue

                row1, col1, row2, col2 = map(int, coords)

                if self.is_valid_move(row1, col1, row2, col2):
                    box_completed = self.draw_line(row1, col1, row2, col2)

                    if not box_completed:
                        self.switch_player()
                    return True
                else:
                    print("Invalid move! Please choose adjacent dots that aren't already connected.")

            except ValueError:
                print("Please enter valid integer numbers.")
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Thanks for playing!")
                return False

    def play_game(self):
        """Main game loop."""
        while not self.game_over:
            self.display_board()

            if not self.play_turn():
                return

            if self.check_game_over():
                self.game_over = True
                self.display_board()
                self.display_final_results()

    def display_final_results(self):
        """Display final scores and winner announcement."""
        winner = self.get_winner()

        print("\n" + "=" * 50)
        print("            GAME OVER!")
        print("=" * 50)
        print(f"Final Scores:")
        print(f"  Player A: {self.scores['A']} points")
        print(f"  Player B: {self.scores['B']} points")

        if winner == 'Tie':
            print("  It's a tie!")
        else:
            print(f"  Player {winner} wins!")
        print("=" * 50)


def get_grid_size():
    """Get grid size from user input."""
    while True:
        try:
            size = input("Enter grid size (e.g., '3' for 3x3, '4' for 4x4, default is 3): ").strip()
            if not size:
                return 3
            size = int(size)
            if 2 <= size <= 8:  # allow a few more sizes if terminal can handle it
                return size
            else:
                print("Please enter a number between 2 and 8.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the game."""
    print("Welcome to Dots and Boxes!")
    print("=" * 50)
    print("Rules:")
    print("- Players take turns connecting adjacent dots")
    print("- Complete a box to score a point and get another turn")
    print("- The player with the most boxes wins")
    print("=" * 50)

    try:
        while True:
            grid_size = get_grid_size()
            game = DotsAndBoxes(rows=grid_size, cols=grid_size)
            game.play_game()

            # Ask if players want to play again
            play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
            if play_again not in ['y', 'yes']:
                print("Thanks for playing! Goodbye!")
                break
    except KeyboardInterrupt:
        print("\n\nGoodbye!")


if __name__ == "__main__":
    main()
