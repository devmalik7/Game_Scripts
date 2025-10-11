import tkinter as tk
import random

# --- Game Settings ---
GRID_SIZE = 3         # 3x3 grid
GAME_TIME = 30        # seconds

class WhackAMole:
    def __init__(self, master):
        self.master = master
        self.master.title("Whack-a-Mole")
        self.score = 0
        self.time_left = GAME_TIME
        self.game_over = False

        self.label_score = tk.Label(master, text=f"Score: {self.score}", font=("Arial", 14))
        self.label_score.grid(row=0, column=0, columnspan=GRID_SIZE)

        self.label_time = tk.Label(master, text=f"Time: {self.time_left}", font=("Arial", 14))
        self.label_time.grid(row=1, column=0, columnspan=GRID_SIZE)

        self.buttons = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                btn = tk.Button(master, width=10, height=4, font=("Arial", 20),
                                command=lambda x=i, y=j: self.hit(x, y))
                btn.grid(row=i+2, column=j)
                row.append(btn)
            self.buttons.append(row)

        self.mole_pos = (-1, -1)
        self.spawn_mole()
        self.update_timer()

    def spawn_mole(self):
        if self.game_over:
            return  # stop spawning moles

        # Remove old mole
        if self.mole_pos != (-1, -1):
            x, y = self.mole_pos
            self.buttons[x][y].config(text="", bg="SystemButtonFace")

        # Spawn new mole
        x = random.randint(0, GRID_SIZE-1)
        y = random.randint(0, GRID_SIZE-1)
        self.mole_pos = (x, y)
        self.buttons[x][y].config(text="😈", bg="lightgreen")

        # spawn a new mole every 1 second
        self.master.after(1000, self.spawn_mole)

    def hit(self, x, y):
        if self.game_over:
            return

        if (x, y) == self.mole_pos:
            self.score += 1
            self.label_score.config(text=f"Score: {self.score}")
            # remove mole immediately after hit
            self.buttons[x][y].config(text="", bg="SystemButtonFace")
            self.mole_pos = (-1, -1)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.label_time.config(text=f"Time: {self.time_left}")
            self.master.after(1000, self.update_timer)
        else:
            # game over
            self.game_over = True
            for row in self.buttons:
                for btn in row:
                    btn.config(state="disabled")
            self.label_time.config(text="Game Over!")

if __name__ == "__main__":
    root = tk.Tk()
    game = WhackAMole(root)
    root.mainloop()
