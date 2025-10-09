import tkinter as tk
import random
from PIL import Image, ImageTk
import time
import os

class DiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Animated Dice Roller")
        self.root.config(bg="#111")

        # Load dice images (ensure they exist in same folder)
        base_path = os.path.dirname(__file__)
        self.dice_images = [
            ImageTk.PhotoImage(Image.open(os.path.join(base_path, f"dice{i}.png")).resize((120, 120)))
            for i in range(1, 7)
        ]

        self.title_label = tk.Label(
            root, text="🎲 Animated Dice Roller", 
            font=("Poppins", 20, "bold"), fg="white", bg="#111"
        )
        self.title_label.pack(pady=20)

        self.dice_label = tk.Label(root, image=self.dice_images[0], bg="#111")
        self.dice_label.pack(pady=20)

        self.result_label = tk.Label(
            root, text="Click below to roll!", 
            font=("Poppins", 14), fg="#ccc", bg="#111"
        )
        self.result_label.pack(pady=10)

        self.roll_button = tk.Button(
            root, text="Roll Dice 🎲", 
            font=("Poppins", 14, "bold"), bg="#4CAF50", fg="white",
            relief="flat", padx=20, pady=10, command=self.animate_roll
        )
        self.roll_button.pack(pady=20)

    def animate_roll(self):
        self.roll_button.config(state="disabled")  # disable during animation

        # Animate by showing random dice faces quickly
        for _ in range(15):  # number of animation frames
            face = random.choice(self.dice_images)
            self.dice_label.config(image=face)
            self.root.update_idletasks()
            time.sleep(0.08)  # control animation speed

        # Final result
        result = random.randint(1, 6)
        self.dice_label.config(image=self.dice_images[result - 1])
        self.result_label.config(text=f"You rolled a {result}!")
        self.roll_button.config(state="normal")  # re-enable button


if __name__ == "__main__":
    root = tk.Tk()
    app = DiceApp(root)
    root.mainloop()
