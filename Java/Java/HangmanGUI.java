/**
 * 🎮 Hangman GUI Game
 *
 * A simple word-guessing game using Java Swing.
 * Players guess letters to figure out a hidden word.
 * GUI displays the current word, remaining attempts, messages, and allows restarting.
 *
 *
 * Author: Pradyumn Pratap Singh (Strange)
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class HangmanGUI extends JFrame implements ActionListener {

    // Array of possible words for the game
    private String[] words = {"JAVA", "HANGMAN", "COMPUTER", "PROGRAMMING", "SWING"};

    // The current word to guess
    private String word;

    // Array to store the current guessed letters (e.g., "_ A _ A")
    private char[] guessedWord;

    // Remaining attempts before the game is over
    private int attempts = 6;

    // Swing components
    private JLabel wordLabel, attemptsLabel, messageLabel;
    private JTextField inputField;
    private JButton guessButton, restartButton;

    /**
     * Constructor to set up the GUI and initialize the game.
     */
    public HangmanGUI() {
        // Select a random word from the list
        word = words[new Random().nextInt(words.length)];

        // Initialize guessedWord array with underscores
        guessedWord = new char[word.length()];
        for (int i = 0; i < guessedWord.length; i++) guessedWord[i] = '_';

        // JFrame properties
        setTitle("🎮 Hangman Game");
        setSize(400, 250);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new GridLayout(5, 1, 5, 5));

        // Label to display the guessed word
        wordLabel = new JLabel(new String(guessedWord), SwingConstants.CENTER);
        wordLabel.setFont(new Font("Segoe UI", Font.BOLD, 24));

        // Label to show remaining attempts
        attemptsLabel = new JLabel("Attempts left: " + attempts, SwingConstants.CENTER);

        // Label to display messages or prompts
        messageLabel = new JLabel("Enter a letter:", SwingConstants.CENTER);

        // Text field for player to enter a guess
        inputField = new JTextField();

        // Buttons for guessing and restarting the game
        guessButton = new JButton("Guess");
        restartButton = new JButton("Restart");

        // Add action listeners
        guessButton.addActionListener(this);
        restartButton.addActionListener(e -> restartGame());

        // Add components to JFrame
        add(wordLabel);
        add(attemptsLabel);
        add(messageLabel);
        add(inputField);

        // Bottom panel for buttons
        JPanel bottomPanel = new JPanel(new FlowLayout());
        bottomPanel.add(guessButton);
        bottomPanel.add(restartButton);
        add(bottomPanel);

        // Make GUI visible
        setVisible(true);
    }

    /**
     * Handles the Guess button click event.
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        String input = inputField.getText().toUpperCase(); // Convert to uppercase
        inputField.setText(""); // Clear input field

        // Validate input
        if (input.length() != 1) {
            messageLabel.setText("Enter only one letter!");
            return;
        }

        char guess = input.charAt(0);
        boolean correct = false;

        // Check if the guessed letter is in the word
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == guess) {
                guessedWord[i] = guess;
                correct = true;
            }
        }

        // Update attempts if guess is incorrect
        if (!correct) attempts--;

        // Update GUI labels
        wordLabel.setText(new String(guessedWord));
        attemptsLabel.setText("Attempts left: " + attempts);

        // Check for win condition
        if (new String(guessedWord).equals(word)) {
            messageLabel.setText("🎉 You Won! Word: " + word);
            guessButton.setEnabled(false);
        }
        // Check for loss condition
        else if (attempts == 0) {
            messageLabel.setText("💀 Game Over! Word: " + word);
            guessButton.setEnabled(false);
        }
    }

    /**
     * Resets the game to start a new round.
     */
    private void restartGame() {
        // Select a new random word
        word = words[new Random().nextInt(words.length)];

        // Reset guessed word
        guessedWord = new char[word.length()];
        for (int i = 0; i < guessedWord.length; i++) guessedWord[i] = '_';

        // Reset attempts
        attempts = 6;

        // Update GUI labels
        wordLabel.setText(new String(guessedWord));
        attemptsLabel.setText("Attempts left: " + attempts);
        messageLabel.setText("Enter a letter:");

        // Enable guess button
        guessButton.setEnabled(true);
    }

    /**
     * Main method to start the game.
     */
    public static void main(String[] args) {
        SwingUtilities.invokeLater(HangmanGUI::new);
    }
}
