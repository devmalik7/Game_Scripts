import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐤 Flappy Bird Clone")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Game variables
gravity = 0.5
bird_movement = 0
game_active = True
score = 0

# Bird setup
bird = pygame.Rect(100, HEIGHT // 2, 34, 24)

# Pipe setup
pipe_width = 70
pipe_height = random.randint(150, 400)
pipe_gap = 150
pipe_list = []

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# Fonts
font = pygame.font.SysFont(None, 50)

def draw_bird():
    pygame.draw.ellipse(screen, YELLOW, bird)

def create_pipe():
    random_pipe_pos = random.randint(150, 400)
    bottom_pipe = pygame.Rect(WIDTH, random_pipe_pos, pipe_width, HEIGHT - random_pipe_pos)
    top_pipe = pygame.Rect(WIDTH, random_pipe_pos - pipe_gap - pipe_height, pipe_width, pipe_height)
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 4
    return [pipe for pipe in pipes if pipe.right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            return False
    if bird.top <= 0 or bird.bottom >= HEIGHT:
        return False
    return True

def show_score(current_score):
    score_surface = font.render(f"Score: {current_score}", True, WHITE)
    screen.blit(score_surface, (10, 10))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 8  # Bird jumps
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird.center = (100, HEIGHT // 2)
                bird_movement = 0
                score = 0
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.fill(BLUE)

    if game_active:
        # Bird
        bird_movement += gravity
        bird.centery += bird_movement
        draw_bird()

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision
        game_active = check_collision(pipe_list)

        # Score (increases when pipes move past bird)
        for pipe in pipe_list:
            if pipe.centerx == bird.centerx:
                score += 0.5
        show_score(int(score))
    else:
        game_over_text = font.render("💥 Game Over!", True, WHITE)
        restart_text = font.render("Press SPACE to Restart", True, WHITE)
        screen.blit(game_over_text, (80, 250))
        screen.blit(restart_text, (30, 300))

    pygame.display.update()
    clock.tick(FPS)
