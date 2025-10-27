import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Mario Platformer")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_width, player_height = 50, 50
player_x, player_y = 100, HEIGHT - player_height - 50
player_vel_x = 5
player_vel_y = 0
jump_height = 15
gravity = 0.8
on_ground = False

# Platforms
platforms = [
    pygame.Rect(0, HEIGHT - 50, WIDTH, 50),      # Ground
    pygame.Rect(200, 450, 200, 20),
    pygame.Rect(500, 350, 200, 20),
]

player = pygame.Rect(player_x, player_y, player_width, player_height)

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_vel_x
    if keys[pygame.K_RIGHT]:
        player.x += player_vel_x
    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = -jump_height
        on_ground = False

    # Apply gravity
    player_vel_y += gravity
    player.y += player_vel_y

    # Collision with platforms
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform) and player_vel_y >= 0:
            player.bottom = platform.top
            player_vel_y = 0
            on_ground = True

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Update display
    pygame.display.flip()
