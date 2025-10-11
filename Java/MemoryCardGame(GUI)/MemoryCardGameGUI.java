/**
 * 🎮 Memory Card Matching Game (GUI)
 *
 * A simple card-matching game using Java Swing.
 * Players flip cards to find matching pairs.  
 * Game ends when all pairs are matched.
 *
 * Complexity:
 * - Time: O(n^2) in worst case for flipping all cards
 * - Space: O(n^2) for storing card states
 *
 * Author: Pradyumn Pratap Singh (Strange)
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Collections;
import java.util.ArrayList;

public class MemoryCardGameGUI extends JFrame implements ActionListener {

    private JButton[] buttons;         // Buttons representing cards
    private String[] cardValues;       // Values for cards
    private int firstIndex = -1;       // First card clicked
    private int secondIndex = -1;      // Second card clicked
    private Timer flipBackTimer;       // Timer to flip back unmatched cards
    private int matchesFound = 0;      // Count of matched pairs

    public MemoryCardGameGUI() {
        setTitle("🎮 Memory Card Matching Game");
        setSize(400, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Grid layout for cards (4x4)
        setLayout(new GridLayout(4, 4, 5, 5));

        buttons = new JButton[16];       // 16 cards
        cardValues = new String[16];

        // Prepare card values (8 pairs)
        ArrayList<String> valuesList = new ArrayList<>();
        for (int i = 1; i <= 8; i++) {
            valuesList.add(String.valueOf(i));
            valuesList.add(String.valueOf(i));
        }
        Collections.shuffle(valuesList); // Shuffle cards
        for (int i = 0; i < 16; i++) cardValues[i] = valuesList.get(i);

        // Initialize buttons
        for (int i = 0; i < 16; i++) {
            buttons[i] = new JButton("?");
            buttons[i].setFont(new Font("Arial", Font.BOLD, 24));
            buttons[i].addActionListener(this);
            add(buttons[i]);
        }

        // Timer for flipping back unmatched cards
        flipBackTimer = new Timer(1000, e -> flipBack());
        flipBackTimer.setRepeats(false);

        setVisible(true);
    }

    /**
     * Handles card clicks
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        JButton clickedButton = (JButton) e.getSource();
        int index = -1;

        // Find index of clicked button
        for (int i = 0; i < buttons.length; i++) {
            if (buttons[i] == clickedButton) {
                index = i;
                break;
            }
        }

        // Ignore clicks if card already matched or currently flipped
        if (buttons[index].getText().equals(cardValues[index]) || flipBackTimer.isRunning()) return;

        // Flip card
        buttons[index].setText(cardValues[index]);

        // Check if first or second card
        if (firstIndex == -1) {
            firstIndex = index;
        } else {
            secondIndex = index;
            // Check for match
            if (cardValues[firstIndex].equals(cardValues[secondIndex])) {
                matchesFound++;
                firstIndex = -1;
                secondIndex = -1;

                // Check if all matches found
                if (matchesFound == 8) {
                    JOptionPane.showMessageDialog(this, "🎉 Congratulations! You matched all pairs!");
                    resetGame();
                }
            } else {
                // Start timer to flip back unmatched cards
                flipBackTimer.start();
            }
        }
    }

    /**
     * Flip back unmatched cards
     */
    private void flipBack() {
        if (firstIndex != -1 && secondIndex != -1) {
            buttons[firstIndex].setText("?");
            buttons[secondIndex].setText("?");
        }
        firstIndex = -1;
        secondIndex = -1;
    }

    /**
     * Reset the game
     */
    private void resetGame() {
        matchesFound = 0;
        firstIndex = -1;
        secondIndex = -1;

        ArrayList<String> valuesList = new ArrayList<>();
        for (int i = 1; i <= 8; i++) {
            valuesList.add(String.valueOf(i));
            valuesList.add(String.valueOf(i));
        }
        Collections.shuffle(valuesList);
        for (int i = 0; i < 16; i++) {
            cardValues[i] = valuesList.get(i);
            buttons[i].setText("?");
        }
    }
}

