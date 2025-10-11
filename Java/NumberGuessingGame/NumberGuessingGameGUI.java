/**
 * 🎮 NumberGuessingGameGUI.java
 * 
 * A simple GUI-based Number Guessing Game using Java Swing.
 * 
 * The computer randomly chooses a number between 1 and 100.
 * The player enters guesses through a text field.
 * The program gives hints: "Too High", "Too Low", or "Correct!"
 * 
 * Features:
 *  ✅ Random number generation
 *  ✅ Real-time feedback via labels
 *  ✅ Guess counter
 *  ✅ Restart button
 * 
 * Time Complexity: O(n) (n = number of guesses)
 * Space Complexity: O(1)
 * 
 * Author: Pradyumn Pratap Singh (Strange)
 * For: Hacktoberfest / Mini Games in Java
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class NumberGuessingGameGUI extends JFrame implements ActionListener {

    private int numberToGuess;
    private int attempts;
    
    private JTextField guessField;
    private JLabel messageLabel;
    private JLabel attemptLabel;
    private JButton guessButton, resetButton;

    public NumberGuessingGameGUI() {
        setTitle("🎯 Number Guessing Game");
        setSize(400, 250);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));

        // Generate random number between 1 and 100
        Random rand = new Random();
        numberToGuess = rand.nextInt(100) + 1;
        attempts = 0;

        // --- UI Components ---
        JLabel title = new JLabel("Guess a Number between 1 and 100", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 18));
        title.setForeground(new Color(30, 144, 255));

        JPanel inputPanel = new JPanel(new FlowLayout());
        JLabel enterLabel = new JLabel("Enter your guess: ");
        guessField = new JTextField(10);
        guessButton = new JButton("Submit");
        resetButton = new JButton("Restart");

        inputPanel.add(enterLabel);
        inputPanel.add(guessField);
        inputPanel.add(guessButton);
        inputPanel.add(resetButton);

        messageLabel = new JLabel("Make your first guess!", SwingConstants.CENTER);
        messageLabel.setFont(new Font("Segoe UI", Font.PLAIN, 14));

        attemptLabel = new JLabel("Attempts: 0", SwingConstants.CENTER);

        // --- Adding Components to Frame ---
        add(title, BorderLayout.NORTH);
        add(inputPanel, BorderLayout.CENTER);
        add(messageLabel, BorderLayout.SOUTH);
        add(attemptLabel, BorderLayout.PAGE_END);

        // --- Event Handling ---
        guessButton.addActionListener(this);
        resetButton.addActionListener(this);

        getContentPane().setBackground(new Color(245, 245, 245));
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == guessButton) {
            String guessText = guessField.getText();
            try {
                int guess = Integer.parseInt(guessText);
                attempts++;
                attemptLabel.setText("Attempts: " + attempts);

                if (guess < 1 || guess > 100) {
                    messageLabel.setText("⚠️ Please enter a number between 1 and 100!");
                } else if (guess < numberToGuess) {
                    messageLabel.setText("📉 Too Low! Try again.");
                } else if (guess > numberToGuess) {
                    messageLabel.setText("📈 Too High! Try again.");
                } else {
                    messageLabel.setText("🎉 Correct! You guessed it in " + attempts + " tries!");
                    guessButton.setEnabled(false);
                }
            } catch (NumberFormatException ex) {
                messageLabel.setText("❌ Invalid input! Please enter a valid number.");
            }
            guessField.setText("");
        }

        if (e.getSource() == resetButton) {
            Random rand = new Random();
            numberToGuess = rand.nextInt(100) + 1;
            attempts = 0;
            guessField.setText("");
            messageLabel.setText("Game restarted! Guess a new number!");
            attemptLabel.setText("Attempts: 0");
            guessButton.setEnabled(true);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(NumberGuessingGameGUI::new);
    }
}
