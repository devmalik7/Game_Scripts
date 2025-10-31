import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# --- Game Settings ---
WIDTH, HEIGHT = 600, 700
ROWS, COLS = 10, 10
MINES_COUNT = 15
TILE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
DARK_GREY = (100, 100, 100)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (50, 50, 255)

# Fonts
FONT = pygame.font.SysFont("arial", 32)
SMALL_FONT = pygame.font.SysFont("arial", 24)

# Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# --- Tile Class ---
class Tile:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE + 100, TILE_SIZE, TILE_SIZE)
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighbor_mines = 0

    def draw(self):
        if self.is_revealed:
            pygame.draw.rect(screen, GREY, self.rect)
            pygame.draw.rect(screen, DARK_GREY, self.rect, 2)
            if self.is_mine:
                pygame.draw.circle(screen, RED, self.rect.center, TILE_SIZE // 4)
            elif self.neighbor_mines > 0:
                num_text = FONT.render(str(self.neighbor_mines), True, BLUE)
                screen.blit(num_text, num_text.get_rect(center=self.rect.center))
        else:
            pygame.draw.rect(screen, DARK_GREY, self.rect)
            pygame.draw.rect(screen, BLACK, self.rect, 2)
            if self.is_flagged:
                flag_text = FONT.render("⚑", True, GREEN)
                screen.blit(flag_text, flag_text.get_rect(center=self.rect.center))

# --- Game Functions ---
def create_grid():
    grid = [[Tile(r, c) for c in range(COLS)] for r in range(ROWS)]
    return grid

def place_mines(grid):
    count = 0
    while count < MINES_COUNT:
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        tile = grid[r][c]
        if not tile.is_mine:
            tile.is_mine = True
            count += 1

def count_neighbor_mines(grid):
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c].is_mine:
                continue
            mine_count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc].is_mine:
                            mine_count += 1
            grid[r][c].neighbor_mines = mine_count

def reveal_tile(grid, row, col):
    tile = grid[row][col]
    if tile.is_revealed or tile.is_flagged:
        return
    tile.is_revealed = True
    if tile.neighbor_mines == 0 and not tile.is_mine:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = row + dr, col + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    reveal_tile(grid, nr, nc)

def check_win(grid):
    for row in grid:
        for tile in row:
            if not tile.is_mine and not tile.is_revealed:
                return False
    return True

def draw_grid(grid):
    screen.fill(WHITE)
    title_text = FONT.render("💣 Minesweeper 💣", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))

    for row in grid:
        for tile in row:
            tile.draw()
    pygame.display.update()

# --- Game Loop ---
def main():
    grid = create_grid()
    place_mines(grid)
    count_neighbor_mines(grid)

    game_over = False
    win = False

    while True:
        draw_grid(grid)
        if game_over:
            msg = "You Lost! 💥" if not win else "You Won! 🎉"
            text = FONT.render(msg, True, RED if not win else GREEN)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 80))
            pygame.display.update()
            pygame.time.delay(2000)
            main()  # Restart game
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                if y < 100:
                    continue
                row = (y - 100) // TILE_SIZE
                col = x // TILE_SIZE
                tile = grid[row][col]

                if event.button == 1:  # Left click
                    if tile.is_mine:
                        tile.is_revealed = True
                        game_over = True
                    else:
                        reveal_tile(grid, row, col)
                        if check_win(grid):
                            game_over = True
                            win = True
                elif event.button == 3:  # Right click
                    tile.is_flagged = not tile.is_flagged

# Run game
if __name__ == "__main__":
    main()
