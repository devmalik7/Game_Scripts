import tkinter as tk
import random
import threading
import time

class MathRush:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Math Rush - Addition Challenge")
        self.root.geometry("400x350")
        self.root.config(bg="#f8f8f8")
        
        self.score = 0
        self.time_left = 10
        self.current_answer = 0

        self.header = tk.Label(root, text="🧮 Math Rush!", font=("Helvetica", 20, "bold"), bg="#f8f8f8", fg="#333")
        self.header.pack(pady=10)

        self.timer_label = tk.Label(root, text="Time left: 10s", font=("Helvetica", 14), fg="#FF5733", bg="#f8f8f8")
        self.timer_label.pack()

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 14), fg="#1E8449", bg="#f8f8f8")
        self.score_label.pack()

        self.question_label = tk.Label(root, text="", font=("Helvetica", 22, "bold"), bg="#f8f8f8")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 16), justify="center")
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind("<Return>", self.check_answer)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f8f8f8")
        self.feedback_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Game", font=("Helvetica", 14, "bold"), bg="#3498db", fg="white", command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        self.score = 0
        self.time_left = 10
        self.score_label.config(text=f"Score: {self.score}")
        self.start_button.config(state="disabled")
        self.feedback_label.config(text="")
        self.next_question()
        self.update_timer()

    def next_question(self):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        self.current_answer = a + b
        self.question_label.config(text=f"{a} + {b} = ?")
        self.answer_entry.delete(0, tk.END)
        self.time_left = 10
        self.timer_label.config(text=f"Time left: {self.time_left}s", fg="#FF5733")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.feedback_label.config(text="⏰ Time's up!", fg="orange")
            self.end_game()

    def check_answer(self, event):
        user_input = self.answer_entry.get().strip()
        if not user_input.isdigit():
            self.feedback_label.config(text="Enter a valid number!", fg="red")
            return
        if int(user_input) == self.current_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.feedback_label.config(text="✅ Correct!", fg="green")
            self.next_question()
        else:
            self.feedback_label.config(text=f"❌ Wrong! Answer was {self.current_answer}", fg="red")
            self.end_game()

    def end_game(self):
        self.question_label.config(text="Game Over!")
        self.start_button.config(state="normal")
        self.feedback_label.config(text=f"Final Score: {self.score}", fg="#333")

if __name__ == "__main__":
    root = tk.Tk()
    game = MathRush(root)
    root.mainloop()
