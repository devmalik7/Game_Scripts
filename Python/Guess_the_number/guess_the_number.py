import random

def choose_difficulty():
    print("\nChoose difficulty level:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 10 attempts)")

    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return 10, 5
        elif choice == "2":
            return 50, 7
        elif choice == "3":
            return 100, 10
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

def play_game():
    print("Welcome to Guess The Number!")
    print("Try to guess the number I'm thinking of...")

    upper_limit, max_attempts = choose_difficulty()
    number_to_guess = random.randint(1, upper_limit)
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nEnter your guess (1-{upper_limit}): "))
            attempts += 1
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print(" Too high! Try again.")

        print(f"Attempts left: {max_attempts - attempts}")

    else:
        print(f"\n💀 Out of attempts! The correct number was {number_to_guess}.")

def main():
    while True:
        play_game()
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
