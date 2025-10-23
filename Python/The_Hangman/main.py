import random
import os

WORDS = {
    'a': "anchor",
    'b': "buffer",
    'c': "canyon",
    'd': "dazzle",
    'e': "ember",
    'f': "fossil",
    'g': "gadget",
    'h': "harvest",
    'i': "ignite",
    'j': "jungle",
    'k': "karate",
    'l': "ladder",
    'm': "marble",
    'n': "nectar",
    'o': "oracle",
    'p': "puzzle",
    'q': "quiver",
    'r': "rocket",
    's': "silver",
    't': "tunnel",
    'u': "urgent",
    'v': "valley",
    'w': "wonder",
    'x': "xylophone",
    'y': "yodel",
    'z': "zealot",
}

HANGMAN_STAGES = [
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

MAX_WRONG_GUESSES = 6


def clear_screen():
    """Clears the terminal screen for a cleaner interface."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_board(word, guessed_letters, wrong_guesses):
    """Displays the current state of the game board."""
    clear_screen()
    print("--- Hangman ---")
    print(HANGMAN_STAGES[wrong_guesses])

    # Display the word with guessed letters revealed
    display_word = " ".join(
        [letter if letter in guessed_letters else "_" for letter in word]
    )
    print(f"Word: {display_word}")
    
    # Show guessed letters that are not in the word
    incorrectly_guessed = sorted([g for g in guessed_letters if g not in word])
    print(f"Incorrect Guesses: {' '.join(incorrectly_guessed)}\n")


def play_game():
    """Main function to run a single Hangman game session."""
    word = random.choice(list(WORDS.values()))
    guessed_letters = {word[0]}  # Automatically reveal the first letter
    wrong_guesses = 0

    clear_screen()
    print("--- Welcome to Hangman! ---")
    print("You have 6 wrong guesses to find the word.")
    input("\nPress Enter to start...")

    while wrong_guesses < MAX_WRONG_GUESSES:
        display_board(word, guessed_letters, wrong_guesses)

        # Check for win condition
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: '{word}'")
            return  # End the game

        guess = input("Guess a letter: ").lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("\nInvalid input. Please enter a single letter.")
            input("Press Enter to continue...")
            continue

        if guess in guessed_letters:
            print("\nYou already guessed that letter!")
            input("Press Enter to continue...")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            wrong_guesses += 1
            print(f"\nWrong! '{guess}' is not in the word.")
            if wrong_guesses < MAX_WRONG_GUESSES:
                input("Press Enter to continue...")

    # If the loop finishes, the player has lost the game
    display_board(word, guessed_letters, wrong_guesses)
    print(f"\nGame over! You ran out of guesses. The word was '{word}'.")


if __name__ == "__main__":
    play_game()
    print("\nThanks for playing The Hangman!")

