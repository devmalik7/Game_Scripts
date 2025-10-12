"""
=====================================
🎯 Throw the Dart - Python Tkinter
=====================================
Author: Revant Singh
Description:
Click the "Throw Dart" button to throw a dart towards the dartboard.
Points are awarded based on how close the dart lands to the bullseye.

Controls:
- Click "Throw Dart" to throw
- Score is calculated automatically

Time Complexity: O(1) per throw
Space Complexity: O(n) where n = number of darts thrown
"""

import tkinter as tk
import random
import math

# ---------------- Game Settings ---------------- #
BOARD_SIZE = 400
DART_RADIUS = 5
NUM_DARTS = 5  # total throws
CENTER = BOARD_SIZE // 2

# Colors
BACKGROUND_COLOR = "#f5f5f5"
BULLSEYE_COLOR = "#ff0000"
BOARD_COLOR = "#00cc00"
DART_COLOR = "#0000ff"

# ---------------- Game Variables ---------------- #
score = 0
throws = 0

# ---------------- Functions ---------------- #
def throw_dart():
    global throws, score

    if throws >= NUM_DARTS:
        result_label.config(text=f"Game Over! Total Score: {score}")
        throw_button.config(state="disabled")
        return

    # Generate dart inside the circular dartboard
    while True:
        x = random.randint(CENTER - 60, CENTER + 60)
        y = random.randint(CENTER - 60, CENTER + 60)
        # check if inside circle radius 60
        if math.sqrt((x - CENTER) ** 2 + (y - CENTER) ** 2) <= 60:
            break

    # Draw dart
    canvas.create_oval(
        x - DART_RADIUS, y - DART_RADIUS,
        x + DART_RADIUS, y + DART_RADIUS,
        fill=DART_COLOR
    )

    # Calculate distance from bullseye
    distance = math.sqrt((x - CENTER) ** 2 + (y - CENTER) ** 2)

    # Score based on distance
    if distance <= 20:
        points = 50
    elif distance <= 40:
        points = 30
    else:
        points = 10

    score += points
    throws += 1
    score_label.config(text=f"Score: {score}")
    turns_label.config(text=f"Darts Left: {NUM_DARTS - throws}")

# ---------------- Main Window ---------------- #
window = tk.Tk()
window.title("🎯 Throw the Dart")
window.resizable(False, False)
window.configure(bg=BACKGROUND_COLOR)

# Canvas for dartboard
canvas = tk.Canvas(window, width=BOARD_SIZE, height=BOARD_SIZE, bg=BACKGROUND_COLOR)
canvas.pack(padx=20, pady=20)

# Draw dartboard (3 circles)
canvas.create_oval(CENTER-60, CENTER-60, CENTER+60, CENTER+60, fill="#66ff66", outline="black")
canvas.create_oval(CENTER-40, CENTER-40, CENTER+40, CENTER+40, fill="#99ff99", outline="black")
canvas.create_oval(CENTER-20, CENTER-20, CENTER+20, CENTER+20, fill=BULLSEYE_COLOR, outline="black")

# Score and turns
score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 14), bg=BACKGROUND_COLOR)
score_label.pack()

turns_label = tk.Label(window, text=f"Darts Left: {NUM_DARTS}", font=("Arial", 14), bg=BACKGROUND_COLOR)
turns_label.pack()

# Result label
result_label = tk.Label(window, text="", font=("Arial", 16, "bold"), bg=BACKGROUND_COLOR)
result_label.pack(pady=10)

# Throw dart button
throw_button = tk.Button(window, text="Throw Dart 🎯", font=("Arial", 14), command=throw_dart)
throw_button.pack(pady=10)

window.mainloop()
