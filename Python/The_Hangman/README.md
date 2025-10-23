# The Hangman

A classic Hangman word-guessing game where the player tries to guess a hidden word before the hangman is fully drawn.

## 🎮 Gameplay & Features

* **Guessing** Try to guess a hidden word, one letter at a time.
* **Hints** The first letter of each word is revealed to the player at the start of the round.
* **Attempts** You have 6 incorrect guesses before the game is over. Each wrong guess draws another part of the hangman figure.
* **Visual Feedback:** The hangman is progressively drawn in the terminal for each wrong guess:
    1.  Head
    2.  Torso
    3.  One Arm
    4.  Second Arm
    5.  One Leg
    6.  Second Leg

## 🚀 How to Run

1.  Navigate to the game's directory from your terminal:
    ```sh
    cd python/hangman
    ```
2.  Run the script using Python:
    ```sh
    python hangman.py
    ```