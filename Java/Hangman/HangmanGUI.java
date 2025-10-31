/**
 * 🎮 Enhanced Hangman GUI Game
 *
 * Features added for Hacktoberfest:
 * ✅ Tracks used letters
 * ✅ Provides hints after 3 wrong guesses
 * ✅ Displays a score system (wins/losses)
 * ✅ Adds color-coded messages for better UX
 *
 * Author: Sakshi (Hacktoberfest Contribution)
 * Original Author: Pradyumn Pratap Singh (Strange)
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

public class HangmanGUI extends JFrame implements ActionListener {

    // Word list with hints
    private final Map<String, String> wordHints = Map.of(
            "JAVA", "A popular programming language",
            "HANGMAN", "A classic word-guessing game",
            "COMPUTER", "An electronic device for calculations",
            "PROGRAMMING", "What developers love to do!",
            "SWING", "A Java GUI toolkit"
    );

    // The current word to guess
    private String word;

    // Array to store guessed letters (e.g., "_ A _ A")
    private char[] guessedWord;

    // Game state variables
    private int attempts = 6;
    private int wins = 0;
    private int losses = 0;
    private Set<Character> usedLetters = new HashSet<>();

    // Swing components
    private JLabel wordLabel, attemptsLabel, messageLabel, usedLabel, scoreLabel;
    private JTextField inputField;
    private JButton guessButton, restartButton;

    /**
     * Constructor to set up the GUI and start the first game.
     */
    public HangmanGUI() {
        setupUI();
        startNewGame();
    }

    /**
     * Initializes GUI components and layout.
     */
    private void setupUI() {
        setTitle("🎮 Enhanced Hangman Game");
        setSize(450, 320);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new GridLayout(7, 1, 5, 5));

        wordLabel = new JLabel("", SwingConstants.CENTER);
        wordLabel.setFont(new Font("Segoe UI", Font.BOLD, 28));

        attemptsLabel = new JLabel("", SwingConstants.CENTER);
        messageLabel = new JLabel("", SwingConstants.CENTER);
        usedLabel = new JLabel("", SwingConstants.CENTER);
        scoreLabel = new JLabel("Score: 0 Wins | 0 Losses", SwingConstants.CENTER);

        inputField = new JTextField();
        guessButton = new JButton("Guess");
        restartButton = new JButton("Restart");

        guessButton.addActionListener(this);
        restartButton.addActionListener(e -> startNewGame());

        JPanel bottomPanel = new JPanel(new FlowLayout());
        bottomPanel.add(guessButton);
        bottomPanel.add(restartButton);

        add(wordLabel);
        add(attemptsLabel);
        add(messageLabel);
        add(inputField);
        add(usedLabel);
        add(scoreLabel);
        add(bottomPanel);

        setVisible(true);
    }

    /**
     * Starts or restarts a new round of the game.
     */
    private void startNewGame() {
        // Pick a random word
        List<String> keys = new ArrayList<>(wordHints.keySet());
        word = keys.get(new Random().nextInt(keys.size()));

        guessedWord = new char[word.length()];
        Arrays.fill(guessedWord, '_');
        attempts = 6;
        usedLetters.clear();

        // Update GUI
        updateLabels();
        messageLabel.setText("Enter a letter:");
        messageLabel.setForeground(Color.BLACK);
        guessButton.setEnabled(true);
        inputField.setText("");
    }

    /**
     * Handles the Guess button click event.
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        String input = inputField.getText().toUpperCase();
        inputField.setText("");

        if (input.length() != 1 || !Character.isLetter(input.charAt(0))) {
            messageLabel.setText("⚠️ Please enter a single letter!");
            messageLabel.setForeground(Color.ORANGE);
            return;
        }

        char guess = input.charAt(0);
        if (usedLetters.contains(guess)) {
            messageLabel.setText("You already tried '" + guess + "'!");
            messageLabel.setForeground(Color.GRAY);
            return;
        }

        usedLetters.add(guess);
        boolean correct = false;

        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == guess) {
                guessedWord[i] = guess;
                correct = true;
            }
        }

        if (!correct) {
            attempts--;
            messageLabel.setText("❌ Wrong! Attempts left: " + attempts);
            messageLabel.setForeground(Color.RED);
        } else {
            messageLabel.setText("✅ Good guess!");
            messageLabel.setForeground(Color.GREEN);
        }

        // Reveal hint if 3 attempts remain
        if (attempts == 3) {
            messageLabel.setText("<html>Hint: " + wordHints.get(word) + "</html>");
            messageLabel.setForeground(new Color(0, 128, 255));
        }

        updateLabels();

        if (new String(guessedWord).equals(word)) {
            wins++;
            messageLabel.setText("🎉 You Won! Word: " + word);
            messageLabel.setForeground(new Color(0, 200, 0));
            guessButton.setEnabled(false);
        } else if (attempts == 0) {
            losses++;
            messageLabel.setText("💀 Game Over! Word: " + word);
            messageLabel.setForeground(Color.RED);
            guessButton.setEnabled(false);
        }

        scoreLabel.setText("Score: " + wins + " Wins | " + losses + " Losses");
    }

    /**
     * Updates labels showing game state.
     */
    private void updateLabels() {
        wordLabel.setText(new String(guessedWord));
        attemptsLabel.setText("Attempts left: " + attempts);
        usedLabel.setText("Used letters: " + usedLetters.toString());
    }

    /**
     * Main method to run the game.
     */
    public static void main(String[] args) {
        SwingUtilities.invokeLater(HangmanGUI::new);
    }
}
