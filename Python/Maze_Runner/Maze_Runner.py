import tkinter as tk
import random

CELL_SIZE = 40
ROWS = 10
COLS = 10
TIME_LIMIT = 60  # seconds

class MazeRunnerValid:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Runner - Valid Random")
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
        self.canvas.pack()

        # Generate maze with guaranteed path
        self.maze = self.generate_maze_with_path(ROWS, COLS)

        # Draw maze
        self.draw_maze()

        # Find start position
        self.player_pos = [0, 0]

        # Draw player
        self.player = self.canvas.create_rectangle(
            10, 10, CELL_SIZE-10, CELL_SIZE-10, fill="blue"
        )

        # Bind keys
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # Timer
        self.time_left = TIME_LIMIT
        self.timer_text = self.canvas.create_text(
            COLS*CELL_SIZE-80, 20, text=f"Time: {self.time_left}", font=("Arial", 14), fill="red"
        )
        self.update_timer()

    def generate_maze_with_path(self, rows, cols):
        maze = [[0 for _ in range(cols)] for _ in range(rows)]

        # Generate a guaranteed path
        path = [(0, 0)]
        r, c = 0, 0
        while (r, c) != (rows-1, cols-1):
            if r == rows-1:
                c += 1
            elif c == cols-1:
                r += 1
            else:
                if random.choice([True, False]):
                    r += 1
                else:
                    c += 1
            path.append((r, c))

        # Add random walls elsewhere (30% chance), but never on the path
        for i in range(rows):
            for j in range(cols):
                if (i, j) in path or (i == rows-1 and j == cols-1):
                    continue
                if random.random() < 0.3:
                    maze[i][j] = 1

        maze[rows-1][cols-1] = "E"  # Exit
        return maze

    def draw_maze(self):
        for r in range(ROWS):
            for c in range(COLS):
                x1, y1 = c*CELL_SIZE, r*CELL_SIZE
                x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
                cell = self.maze[r][c]
                if cell == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                elif cell == "E":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")

    def move_player(self, dr, dc):
        new_r = self.player_pos[0] + dr
        new_c = self.player_pos[1] + dc
        if 0 <= new_r < ROWS and 0 <= new_c < COLS:
            if self.maze[new_r][new_c] != 1:
                self.player_pos = [new_r, new_c]
                self.canvas.coords(
                    self.player,
                    new_c*CELL_SIZE+10,
                    new_r*CELL_SIZE+10,
                    new_c*CELL_SIZE+CELL_SIZE-10,
                    new_r*CELL_SIZE+CELL_SIZE-10
                )
                if self.maze[new_r][new_c] == "E":
                    self.end_game(win=True)

    def move_up(self, event): self.move_player(-1, 0)
    def move_down(self, event): self.move_player(1, 0)
    def move_left(self, event): self.move_player(0, -1)
    def move_right(self, event): self.move_player(0, 1)

    def update_timer(self):
        self.time_left -= 1
        self.canvas.itemconfig(self.timer_text, text=f"Time: {self.time_left}")
        if self.time_left <= 0:
            self.end_game(win=False)
        else:
            self.root.after(1000, self.update_timer)

    def end_game(self, win):
        msg = "You Win!" if win else "Time's Up! Game Over!"
        self.canvas.create_text(
            COLS*CELL_SIZE//2, ROWS*CELL_SIZE//2,
            text=msg, font=("Arial", 24), fill="red"
        )
        self.root.unbind("<Up>")
        self.root.unbind("<Down>")
        self.root.unbind("<Left>")
        self.root.unbind("<Right>")

if __name__ == "__main__":
    root = tk.Tk()
    game = MazeRunnerValid(root)
    root.mainloop()
