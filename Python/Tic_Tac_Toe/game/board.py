"""
Game board logic and state management.
"""


class Board:
    """Manages the game board state and win detection."""

    def __init__(self):
        """Initialize an empty 3x3 board."""
        self.cells = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def reset(self):
        """Reset the board to initial state."""
        self.cells = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def is_valid_move(self, row, col):
        """
        Check if a move is valid.

        Args:
            row: Row index (0-2)
            col: Column index (0-2)

        Returns:
            bool: True if the move is valid, False otherwise
        """
        if not (0 <= row < 3 and 0 <= col < 3):
            return False
        return self.cells[row][col] == ""

    def make_move(self, row, col):
        """
        Make a move on the board.

        Args:
            row: Row index (0-2)
            col: Column index (0-2)

        Returns:
            bool: True if move was successful, False otherwise
        """
        if not self.is_valid_move(row, col):
            return False

        self.cells[row][col] = self.current_player
        return True

    def switch_player(self):
        """Switch to the other player."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """
        Check if there's a winner.

        Returns:
            tuple: (winner, winning_combo) where winner is 'X', 'O', or None
                   winning_combo is a tuple like ('row', 0), ('col', 1), ('diag', 0)
        """
        # Check rows
        for i in range(3):
            if (
                self.cells[i][0] == self.cells[i][1] == self.cells[i][2] != ""
            ):
                return self.cells[i][0], ("row", i)

        # Check columns
        for i in range(3):
            if (
                self.cells[0][i] == self.cells[1][i] == self.cells[2][i] != ""
            ):
                return self.cells[0][i], ("col", i)

        # Check diagonals
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] != "":
            return self.cells[0][0], ("diag", 0)

        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] != "":
            return self.cells[0][2], ("diag", 1)

        return None, None

    def is_full(self):
        """
        Check if the board is full.

        Returns:
            bool: True if board is full, False otherwise
        """
        for row in self.cells:
            if "" in row:
                return False
        return True

    def get_cell(self, row, col):
        """
        Get the value of a cell.

        Args:
            row: Row index (0-2)
            col: Column index (0-2)

        Returns:
            str: 'X', 'O', or '' (empty)
        """
        if 0 <= row < 3 and 0 <= col < 3:
            return self.cells[row][col]
        return None
