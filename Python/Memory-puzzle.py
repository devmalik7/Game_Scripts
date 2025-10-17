import tkinter as tk
import random
from functools import partial

# Create main window
root = tk.Tk()
root.title("🧠 Memory Puzzle Game")
root.geometry("400x400")

# Game variables
buttons = []
first_choice = None
second_choice = None
pairs_found = 0
moves = 0

# Symbols (8 pairs for 16 cards)
symbols = list("AABBCCDDEEFFGGHH")
random.shuffle(symbols)

# Functions
def check_match(btn, symbol):
    global first_choice, second_choice, pairs_found, moves

    btn.config(text=symbol, state="disabled", disabledforeground="black")

    if not first_choice:
        first_choice = (btn, symbol)
    elif not second_choice:
        second_choice = (btn, symbol)
        root.after(500, evaluate_match)

def evaluate_match():
    global first_choice, second_choice, pairs_found, moves

    moves += 1
    btn1, sym1 = first_choice
    btn2, sym2 = second_choice

    if sym1 != sym2:
        btn1.config(text="", state="normal")
        btn2.config(text="", state="normal")
    else:
        pairs_found += 1

    first_choice = None
    second_choice = None

    if pairs_found == 8:
        win_label = tk.Label(root, text=f"🎉 You won in {moves} moves!", font=("Arial", 16))
        win_label.pack(pady=20)

# Create buttons (4x4 grid)
for i in range(4):
    row = []
    for j in range(4):
        index = i*4 + j
        btn = tk.Button(root, text="", width=6, height=3,
                        command=partial(check_match, btn=None, symbol=symbols[index]))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Fix button references (needed for partial)
flat_buttons = [btn for row in buttons for btn in row]
for i, btn in enumerate(flat_buttons):
    btn.config(command=partial(check_match, btn, symbols[i]))

root.mainloop()
