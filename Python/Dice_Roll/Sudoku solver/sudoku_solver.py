"""
sudoku_solver.py
----------------
A Sudoku solver using backtracking, with optional Tkinter GUI visualization.

Usage:
    python sudoku_solver.py          # Solves a sample Sudoku in console
    python sudoku_solver.py gui      # Opens GUI to visualize solving
"""

import time
import sys
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Core Backtracking Solver
# -----------------------------

def print_board(board):
    for i in range(9):
        row = ""
        for j in range(9):
            row += str(board[i][j]) + " "
            if (j + 1) % 3 == 0 and j < 8:
                row += "| "
        print(row)
        if (i + 1) % 3 == 0 and i < 8:
            print("- " * 11)
    print()


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, row, col, num):
    # Row
    if num in board[row]:
        return False
    # Column
    if num in [board[i][col] for i in range(9)]:
        return False
    # 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True


def solve(board, visualize_callback=None, delay=0.05):
    """Solves the Sudoku using backtracking."""
    find = find_empty(board)
    if not find:
        return True
    row, col = find

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if visualize_callback:
                visualize_callback(board)
                time.sleep(delay)

            if solve(board, visualize_callback, delay):
                return True

            board[row][col] = 0
            if visualize_callback:
                visualize_callback(board)
                time.sleep(delay)

    return False


# -----------------------------
# Tkinter GUI Visualization
# -----------------------------

class SudokuGUI:
    def __init__(self, root, board):
        self.root = root
        self.root.title("Sudoku Solver (Backtracking Visualization)")
        self.board = [row[:] for row in board]
        self.cells = [[None for _ in range(9)] for _ in range(9)]

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.build_grid()

        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.pack(pady=5)

    def build_grid(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(
                    self.frame,
                    width=2,
                    font=("Arial", 18),
                    justify="center",
                    borderwidth=1,
                    relief="solid",
                )
                entry.grid(row=i, column=j, padx=1, pady=1, ipadx=5, ipady=5)
                if self.board[i][j] != 0:
                    entry.insert(0, str(self.board[i][j]))
                    entry.config(state="disabled", disabledforeground="black")
                # Thicker borders for 3x3 boxes
                if i % 3 == 0 and i != 0:
                    entry.grid(pady=(4, 1))
                if j % 3 == 0 and j != 0:
                    entry.grid(padx=(4, 1))
                self.cells[i][j] = entry

    def update_grid(self, board):
        for i in range(9):
            for j in range(9):
                cell = self.cells[i][j]
                if cell["state"] == "normal":
                    val = board[i][j]
                    cell.delete(0, tk.END)
                    if val != 0:
                        cell.insert(0, str(val))
                    cell.update()

    def solve(self):
        start = time.time()
        solved = solve(self.board, self.update_grid, delay=0.02)
        end = time.time()
        if solved:
            messagebox.showinfo("Sudoku Solver", f"Solved in {end - start:.2f} seconds!")
        else:
            messagebox.showerror("Sudoku Solver", "No solution found.")


# -----------------------------
# Example Sudoku & Main Entry
# -----------------------------

def sample_board():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() == "gui":
        root = tk.Tk()
        SudokuGUI(root, sample_board())
        root.mainloop()
    else:
        board = sample_board()
        print("Initial Sudoku:")
        print_board(board)
        start = time.time()
        if solve(board):
            end = time.time()
            print("Solved Sudoku:")
            print_board(board)
            print(f"Solved in {end - start:.3f} seconds.")
        else:
            print("No solution exists.")


if __name__ == "__main__":
    main()
