import tkinter as tk
import random

# Game constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_RADIUS = 10
BRICK_ROWS = 5
BRICK_COLUMNS = 8
BRICK_WIDTH = 70
BRICK_HEIGHT = 20
BALL_SPEED = 4

class BrickBreaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Brick Breaker")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()
        
        # Paddle
        self.paddle = self.canvas.create_rectangle(
            (WINDOW_WIDTH-PADDLE_WIDTH)//2, WINDOW_HEIGHT-30,
            (WINDOW_WIDTH+PADDLE_WIDTH)//2, WINDOW_HEIGHT-30+PADDLE_HEIGHT,
            fill="blue"
        )
        
        # Ball
        self.ball = self.canvas.create_oval(
            WINDOW_WIDTH//2-BALL_RADIUS, WINDOW_HEIGHT//2-BALL_RADIUS,
            WINDOW_WIDTH//2+BALL_RADIUS, WINDOW_HEIGHT//2+BALL_RADIUS,
            fill="red"
        )
        self.ball_dx = BALL_SPEED
        self.ball_dy = -BALL_SPEED
        
        # Bricks
        self.bricks = []
        colors = ["red","orange","yellow","green","cyan"]
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLUMNS):
                x1 = col * (BRICK_WIDTH+5) + 35
                y1 = row * (BRICK_HEIGHT+5) + 50
                x2 = x1 + BRICK_WIDTH
                y2 = y1 + BRICK_HEIGHT
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colors[row % len(colors)], tags="brick")
                self.bricks.append(brick)
        
        self.score = 0
        self.score_text = self.canvas.create_text(50, 20, text="Score: 0", fill="white", font=("Arial", 14))
        
        # Bind mouse movement
        self.canvas.bind("<Motion>", self.move_paddle)
        self.root.after(20, self.game_loop)
    
    def move_paddle(self, event):
        x = event.x
        if x < PADDLE_WIDTH//2:
            x = PADDLE_WIDTH//2
        elif x > WINDOW_WIDTH - PADDLE_WIDTH//2:
            x = WINDOW_WIDTH - PADDLE_WIDTH//2
        self.canvas.coords(self.paddle, x-PADDLE_WIDTH//2, WINDOW_HEIGHT-30, x+PADDLE_WIDTH//2, WINDOW_HEIGHT-30+PADDLE_HEIGHT)
    
    def game_loop(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)
        ball_left, ball_top, ball_right, ball_bottom = ball_coords
        
        # Wall collisions
        if ball_left <= 0 or ball_right >= WINDOW_WIDTH:
            self.ball_dx *= -1
        if ball_top <= 0:
            self.ball_dy *= -1
        if ball_bottom >= WINDOW_HEIGHT:
            self.game_over("Game Over!")
            return
        
        # Paddle collision
        paddle_coords = self.canvas.coords(self.paddle)
        if self.check_collision(ball_coords, paddle_coords):
            self.ball_dy *= -1
        
        # Brick collisions
        for brick in self.bricks:
            if self.check_collision(ball_coords, self.canvas.coords(brick)):
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.ball_dy *= -1
                self.score += 10
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                break
        
        if len(self.bricks) == 0:
            self.game_over("You Win!")
            return
        
        self.root.after(20, self.game_loop)
    
    def check_collision(self, ball_coords, rect_coords):
        ball_left, ball_top, ball_right, ball_bottom = ball_coords
        rect_left, rect_top, rect_right, rect_bottom = rect_coords
        return not (ball_right < rect_left or ball_left > rect_right or ball_bottom < rect_top or ball_top > rect_bottom)
    
    def game_over(self, message):
        self.canvas.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, text=message, fill="white", font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = BrickBreaker(root)
    root.mainloop()
