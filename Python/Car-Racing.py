import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏎️ Top-Down Car Racing")

# Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (200, 0, 0)
GREEN = (0, 200, 0)

# Load player car image
PLAYER_CAR = pygame.Surface((50, 100))
PLAYER_CAR.fill(GREEN)

# Load enemy car image
ENEMY_CAR = pygame.Surface((50, 100))
ENEMY_CAR.fill(RED)

# Player car position
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 120
player_speed = 5

# Enemy cars
enemy_speed = 5
enemy_list = []

def add_enemy():
    x_pos = random.randint(50, WIDTH - 100)
    y_pos = -100
    enemy_list.append([x_pos, y_pos])

def draw_enemies():
    for enemy in enemy_list:
        screen.blit(ENEMY_CAR, (enemy[0], enemy[1]))

def move_enemies():
    global enemy_list
    for enemy in enemy_list:
        enemy[1] += enemy_speed
    # Remove enemies that have left the screen
    enemy_list = [enemy for enemy in enemy_list if enemy[1] < HEIGHT]

def check_collision():
    for enemy in enemy_list:
        if (player_y < enemy[1] + 100 and player_y + 100 > enemy[1]) and \
           (player_x < enemy[0] + 50 and player_x + 50 > enemy[0]):
            return True
    return False

# Score
score = 0
font = pygame.font.SysFont(None, 40)

def show_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Main game loop
running = True
enemy_timer = 0  # Timer to add new enemies

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    # Enemy logic
    enemy_timer += 1
    if enemy_timer > 50:  # add new enemy every ~50 frames
        add_enemy()
        enemy_timer = 0

    move_enemies()
    draw_enemies()

    # Draw player
    screen.blit(PLAYER_CAR, (player_x, player_y))

    # Collision check
    if check_collision():
        print("💥 Game Over! Your score:", score)
        pygame.quit()
        sys.exit()

    # Update score
    score += 1
    show_score()

    pygame.display.update()
    clock.tick(FPS)
