import random

def get_computer_choice():
    """Returns rock, paper, or scissors randomly for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    """Determines the winner of a round."""
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def main():
    print("🎮 Welcome to Rock–Paper–Scissors! 🎮")
    print("Type 'rock', 'paper', or 'scissors'. Type 'q' to quit.\n")

    player_score = 0
    computer_score = 0

    while True:
        player = input("Your move: ").strip().lower()
        if player == 'q':
            break
        if player not in ["rock", "paper", "scissors"]:
            print("❌ Invalid input. Try again!\n")
            continue

        computer = get_computer_choice()
        print(f"Computer chose: {computer}")

        result = determine_winner(player, computer)
        if result == "player":
            print("✅ You win this round!\n")
            player_score += 1
        elif result == "computer":
            print("💻 Computer wins this round!\n")
            computer_score += 1
        else:
            print("🤝 It's a tie!\n")

    print(f"Final Score — You: {player_score}, Computer: {computer_score}")
    print("Thanks for playing! 👋")

if __name__ == "__main__":
    main()
