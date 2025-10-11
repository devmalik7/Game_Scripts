# treasure_hunt.py

def main():
    print("Treasure Hunt — a tiny text adventure.")
    print("You're at the edge of a forest. You can go 'left' (toward a river) or 'right' (toward a cave).")
    choice1 = input("Choose (left/right): ").strip().lower()
    if choice1 == "left":
        print("You reach a river with a rickety bridge and a boat.")
        c = input("Do you 'cross' the bridge or 'use' the boat? ").strip().lower()
        if c == "cross":
            print("The bridge collapses — but you hang on and climb to safety. You find a chest on the other side. You win!")
        elif c == "use":
            print("Boat had a leak, you swim and find a shiny coin but no treasure. Game over.")
        else:
            print("Indecision costs time; a storm forces you back. Game over.")
    elif choice1 == "right":
        print("You enter a cave. It's dark and you see two tunnels: 'up' and 'down'.")
        c = input("Choose tunnel (up/down): ").strip().lower()
        if c == "up":
            print("You find a hidden chamber filled with treasure. Congrats — you win!")
        elif c == "down":
            print("You find bats and get chased out. Game over.")
        else:
            print("You wander and return empty-handed. Game over.")
    else:
        print("You sit and wait — nothing happens. Game over.")

if __name__ == "__main__":
    main()
