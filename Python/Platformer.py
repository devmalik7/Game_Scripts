import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏃 Platformer Game")

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE  = (135, 206, 250)
GREEN = (0, 200, 0)
RED   = (200, 0, 0)

# Player setup
player_width = 50
player_height = 60
player_x = 100
player_y = HEIGHT - player_height - 50
player_velocity_y = 0
player_speed = 5
jump_force = 15
gravity = 0.8
on_ground = False

player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# Platforms
platforms = [
    pygame.Rect(0, HEIGHT-40, WIDTH, 40),       # ground
    pygame.Rect(200, HEIGHT-150, 150, 20),
    pygame.Rect(450, HEIGHT-250, 150, 20),
    pygame.Rect(650, HEIGHT-350, 120, 20)
]

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLUE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_SPACE] and on_ground:
        player_velocity_y = -jump_force
        on_ground = False

    # Apply gravity
    player_velocity_y += gravity
    player_rect.y += player_velocity_y

    # Collision with platforms
    on_ground = False
    for platform in platforms:
        if player_rect.colliderect(platform) and player_velocity_y > 0:
            player_rect.bottom = platform.top
            player_velocity_y = 0
            on_ground = True

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    # Draw player
    pygame.draw.rect(screen, RED, player_rect)

    pygame.display.update()
