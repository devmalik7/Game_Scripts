import random

# Dungeon size
ROWS, COLS = 5, 5

# Symbols
EMPTY, PLAYER, EXIT, TRAP = '.', 'P', 'E', 'X'

def create_dungeon():
    dungeon = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    exit_row, exit_col = random.randint(0, ROWS-1), random.randint(0, COLS-1)
    dungeon[exit_row][exit_col] = EXIT

    # Random traps
    for _ in range(5):
        r, c = random.randint(0, ROWS-1), random.randint(0, COLS-1)
        if dungeon[r][c] == EMPTY:
            dungeon[r][c] = TRAP

    # Place player
    while True:
        pr, pc = random.randint(0, ROWS-1), random.randint(0, COLS-1)
        if dungeon[pr][pc] == EMPTY:
            dungeon[pr][pc] = PLAYER
            break
    return dungeon, pr, pc

def display_dungeon(dungeon):
    for row in dungeon:
        print(' '.join(row))
    print()

def move_player(dungeon, pr, pc, direction):
    dungeon[pr][pc] = EMPTY
    if direction == 'N': pr -= 1
    elif direction == 'S': pr += 1
    elif direction == 'E': pc += 1
    elif direction == 'W': pc -= 1
    pr, pc = max(0, min(ROWS-1, pr)), max(0, min(COLS-1, pc))
    cell = dungeon[pr][pc]
    dungeon[pr][pc] = PLAYER
    return pr, pc, cell

def play():
    dungeon, pr, pc = create_dungeon()
    lives = 3

    print("🏰 Welcome to Dungeon Escape!")
    print("Find the exit (E) and avoid traps (X). Move with N/S/E/W.\n")

    while True:
        display_dungeon(dungeon)
        move = input("Move (N/S/E/W): ").upper()
        if move not in ['N', 'S', 'E', 'W']:
            print("Invalid move. Try again.")
            continue

        pr, pc, cell = move_player(dungeon, pr, pc, move)

        if cell == EXIT:
            display_dungeon(dungeon)
            print("🎉 You escaped the dungeon! You win!")
            break
        elif cell == TRAP:
            lives -= 1
            print(f"💀 You hit a trap! Lives left: {lives}")
            if lives == 0:
                print("Game Over! You couldn’t escape.")
                break

if __name__ == "__main__":
    play()
