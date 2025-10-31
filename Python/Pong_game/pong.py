import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏓 Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font_large = pygame.font.Font(None, 100)
font_medium = pygame.font.Font(None, 60)
font_small = pygame.font.Font(None, 40)

# Game settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
PADDLE_SPEED = 7
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Create paddles and ball
player = pygame.Rect(WIDTH - 20, HEIGHT//2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(10, HEIGHT//2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - 10, HEIGHT//2 - 10, BALL_SIZE, BALL_SIZE)

# Score
player_score = 0
opponent_score = 0

clock = pygame.time.Clock()

# Game state
menu_active = True
mode_selected = None  # "pve" or "pvp"

def draw_text(text, font, color, surface, x, y):
    """Helper function to draw text centered."""
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def main_menu():
    """Display start menu."""
    global menu_active, mode_selected
    while menu_active:
        screen.fill(BLACK)
        draw_text("PONG", font_large, WHITE, screen, WIDTH/2, HEIGHT/4)
        draw_text("1. Player vs Computer", font_medium, WHITE, screen, WIDTH/2, HEIGHT/2 - 30)
        draw_text("2. Player vs Player", font_medium, WHITE, screen, WIDTH/2, HEIGHT/2 + 40)
        draw_text("ESC to Quit", font_small, WHITE, screen, WIDTH/2, HEIGHT - 50)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode_selected = "pve"
                    menu_active = False
                elif event.key == pygame.K_2:
                    mode_selected = "pvp"
                    menu_active = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def game_loop(mode):
    """Main game loop."""
    global player_score, opponent_score
    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y
    player_score = 0
    opponent_score = 0

    # Reset positions
    player.centery = HEIGHT // 2
    opponent.centery = HEIGHT // 2
    ball.center = (WIDTH // 2, HEIGHT // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # Return to menu

        # Paddle movement
        keys = pygame.key.get_pressed()
        # Player 1
        if keys[pygame.K_UP] and player.top > 0:
            player.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
            player.y += PADDLE_SPEED

        # Opponent / Player 2
        if mode == "pve":
            # Simple AI: follow the ball
            if opponent.centery < ball.centery:
                opponent.y += PADDLE_SPEED
            if opponent.centery > ball.centery:
                opponent.y -= PADDLE_SPEED
        else:  # PvP
            if keys[pygame.K_w] and opponent.top > 0:
                opponent.y -= PADDLE_SPEED
            if keys[pygame.K_s] and opponent.bottom < HEIGHT:
                opponent.y += PADDLE_SPEED

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Collision with top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        # Collision with paddles
        if ball.colliderect(player) or ball.colliderect(opponent):
            ball_speed_x *= -1

        # Score update
        if ball.left <= 0:
            player_score += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_speed_x *= -1
        if ball.right >= WIDTH:
            opponent_score += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_speed_x *= -1

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, WHITE, opponent)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

        # Scores
        player_text = font_medium.render(str(player_score), True, WHITE)
        opponent_text = font_medium.render(str(opponent_score), True, WHITE)
        screen.blit(player_text, (WIDTH//2 + 40, 20))
        screen.blit(opponent_text, (WIDTH//2 - 80, 20))

        # Escape hint
        draw_text("ESC to return to menu", font_small, WHITE, screen, WIDTH/2, HEIGHT - 40)

        pygame.display.flip()
        clock.tick(60)

# Run the game
while True:
    main_menu()
    game_loop(mode_selected)
    menu_active = True
