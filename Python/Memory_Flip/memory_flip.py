import tkinter as tk
import random
from functools import partial

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Memory Flip Game")
        self.cards = list('AABBCCDDEEFF')
        random.shuffle(self.cards)
        self.buttons = []
        self.flipped = []
        self.create_board()
        self.matched = 0

    def create_board(self):
        for i in range(4):
            row = []
            for j in range(3):
                btn = tk.Button(self.root, text='❓', width=8, height=4, 
                                command=partial(self.flip_card, i, j))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def flip_card(self, i, j):
        idx = i * 3 + j
        btn = self.buttons[i][j]
        if btn['text'] == '❓' and len(self.flipped) < 2:
            btn['text'] = self.cards[idx]
            self.flipped.append((i, j))
        if len(self.flipped) == 2:
            self.root.after(800, self.check_match)

    def check_match(self):
        (i1, j1), (i2, j2) = self.flipped
        b1, b2 = self.buttons[i1][j1], self.buttons[i2][j2]
        if b1['text'] == b2['text']:
            b1['state'] = b2['state'] = 'disabled'
            self.matched += 2
            if self.matched == len(self.cards):
                tk.Label(self.root, text="🎉 You won!", font=('Arial', 14)).grid(row=5, column=0, columnspan=3)
        else:
            b1['text'] = b2['text'] = '❓'
        self.flipped.clear()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()