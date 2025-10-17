import pygame, sys, random

# Initialize pygame
pygame.init()
pygame.display.set_caption("🐍 Snake Game - Enhanced Edition")

# Screen setup
CELL_SIZE = 25
GRID_SIZE = 25
WIDTH, HEIGHT = CELL_SIZE * GRID_SIZE, CELL_SIZE * GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (220, 20, 60)
WHITE = (255, 255, 255)
LIGHT_GRAY = (40, 40, 40)
BLACK = (0, 0, 0)
BG_TOP = (10, 10, 30)
BG_BOTTOM = (30, 30, 60)

# Fonts
font = pygame.font.SysFont("consolas", 28, bold=True)
big_font = pygame.font.SysFont("consolas", 50, bold=True)

# Game state
snake = [(12, 12), (11, 12), (10, 12)]
direction = (1, 0)
food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
score = 0
speed = 10
game_over = False

def draw_gradient_background():
    for y in range(HEIGHT):
        color = (
            BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * y // HEIGHT,
            BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * y // HEIGHT,
            BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * y // HEIGHT
        )
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, LIGHT_GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, LIGHT_GRAY, (0, y), (WIDTH, y))

def draw_snake():
    for i, pos in enumerate(snake):
        color = DARK_GREEN if i == 0 else GREEN
        pygame.draw.rect(screen, color,
                         (pos[0] * CELL_SIZE + 2, pos[1] * CELL_SIZE + 2,
                          CELL_SIZE - 4, CELL_SIZE - 4))

def draw_food():
    pygame.draw.circle(screen, RED,
                       (food[0] * CELL_SIZE + CELL_SIZE // 2,
                        food[1] * CELL_SIZE + CELL_SIZE // 2),
                       CELL_SIZE // 2 - 3)

def show_text(text, size, color, center):
    font_obj = pygame.font.SysFont("consolas", size, bold=True)
    label = font_obj.render(text, True, color)
    rect = label.get_rect(center=center)
    screen.blit(label, rect)

def reset_game():
    global snake, direction, food, score, speed, game_over
    snake = [(12, 12), (11, 12), (10, 12)]
    direction = (1, 0)
    food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    score = 0
    speed = 10
    game_over = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)
            elif event.key == pygame.K_r and game_over:
                reset_game()

    if not game_over:
        # Move snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if (new_head in snake or
            not (0 <= new_head[0] < GRID_SIZE) or
            not (0 <= new_head[1] < GRID_SIZE)):
            game_over = True
        else:
            snake.insert(0, new_head)
            if new_head == food:
                score += 10
                speed = min(20, speed + 0.5)
                food = (random.randint(0, GRID_SIZE - 1),
                        random.randint(0, GRID_SIZE - 1))
            else:
                snake.pop()

    # Draw everything
    draw_gradient_background()
    draw_grid()
    draw_snake()
    draw_food()

    if not game_over:
        score_label = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_label, (10, 10))
    else:
        show_text("GAME OVER", 60, RED, (WIDTH // 2, HEIGHT // 2 - 30))
        show_text(f"Final Score: {score}", 35, WHITE, (WIDTH // 2, HEIGHT // 2 + 20))
        show_text("Press R to Restart", 25, (180, 180, 180), (WIDTH // 2, HEIGHT // 2 + 70))

    pygame.display.flip()
    clock.tick(speed)
