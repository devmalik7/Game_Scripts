"""
=====================================
🐍 Snake Game - Python (Tkinter GUI)
=====================================
Author: Revant Singh
Description:
A fun Snake Game built using Tkinter.
Use arrow keys to move the snake and
eat red food to grow longer and increase score.

-------------------------------------
🎮 Controls:
- ⬆️ Up Arrow    → Move Up
- ⬇️ Down Arrow  → Move Down
- ⬅️ Left Arrow  → Move Left
- ➡️ Right Arrow → Move Right
-------------------------------------

Time Complexity: O(1) per frame
Space Complexity: O(n) where n = snake length
"""

import tkinter as tk
import random

# Game settings
GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 100       # milliseconds per move
SPACE_SIZE = 20   # size of each grid block
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND = "#1a1a1a"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 10
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}

    if new_direction != opposites.get(direction):
        direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    # Hit wall
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    # Hit itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete("all")
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2,
                       text=f"GAME OVER\nScore: {score}",
                       fill="white", font=("Consolas", 24, "bold"))

# ---------------- Main ---------------- #
window = tk.Tk()
window.title("🐍 Snake Game by Revant")
window.resizable(False, False)

score = 0
direction = "down"

label = tk.Label(window, text=f"Score: {score}", font=("Consolas", 16))
label.pack()

canvas = tk.Canvas(window, bg=BACKGROUND, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
