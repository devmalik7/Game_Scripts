import tkinter as tk
import time
import random

# Sentences pool
sentences = [
    "Python is powerful and easy to learn.",
    "Typing fast helps improve productivity.",
    "Keep practicing to increase your speed.",
    "Focus on accuracy before speed.",
    "Consistency is the key to mastery.",
    "Coding improves logical thinking.",
]

class TypingSpeedGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Challenge (30 Seconds)")
        self.root.geometry("600x350")
        self.root.config(bg="#f7f7f7")
        self.root.resizable(False, False)

        self.text = random.choice(sentences)
        self.time_left = 30
        self.start_time = None
        self.running = False

        # Title
        tk.Label(root, text="⌨️ Typing Speed Challenge", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#222").pack(pady=10)

        # Instruction
        tk.Label(root, text="You have 30 seconds! Type the sentence below and press [Enter] to finish early.",
                 font=("Arial", 10), bg="#f7f7f7", fg="#555").pack()

        # Sentence to type
        self.label = tk.Label(root, text=self.text, wraplength=500, font=("Arial", 14), bg="#f7f7f7", fg="#333")
        self.label.pack(pady=15)

        # Typing box
        self.entry = tk.Entry(root, width=60, font=("Arial", 14), bd=2, relief="solid", justify="center")
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)
        self.entry.bind("<Return>", self.finish)

        # Timer display
        self.timer_label = tk.Label(root, text="Time Left: 30s", font=("Arial", 12, "bold"), bg="#f7f7f7", fg="#cc0000")
        self.timer_label.pack(pady=5)

        # Result display
        self.result = tk.Label(root, text="", font=("Arial", 13, "bold"), bg="#f7f7f7", fg="#007700")
        self.result.pack(pady=10)

        # Restart button
        self.restart_btn = tk.Button(root, text="Restart", font=("Arial", 12), bg="#007bff", fg="white", command=self.restart)
        self.restart_btn.pack(pady=10)

        self.entry.focus_set()

    def start_timer(self, event):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.countdown()

    def countdown(self):
        if self.time_left > 0 and self.running:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.countdown)
        else:
            self.finish(None)

    def finish(self, event):
        if not self.running:
            return
        self.running = False

        typed = self.entry.get().strip()
        end_time = time.time()
        elapsed = end_time - self.start_time if self.start_time else 0.1

        # Calculate results
        words_typed = len(typed.split())
        words_per_minute = (words_typed / elapsed) * 60
        correct_chars = sum(a == b for a, b in zip(self.text, typed))
        accuracy = (correct_chars / len(self.text)) * 100

        # Display results
        self.result.config(text=f"⏱️ Time's up!\nSpeed: {words_per_minute:.0f} WPM | Accuracy: {accuracy:.0f}%")

    def restart(self):
        self.text = random.choice(sentences)
        self.label.config(text=self.text)
        self.entry.delete(0, tk.END)
        self.result.config(text="")
        self.time_left = 30
        self.timer_label.config(text="Time Left: 30s")
        self.running = False
        self.start_time = None
        self.entry.focus_set()

# Run the app
root = tk.Tk()
app = TypingSpeedGame(root)
root.mainloop()
