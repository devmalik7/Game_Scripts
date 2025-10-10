/**
 * 🎮 TicTacToeGUI.java
 *
 * A simple GUI-based Tic Tac Toe game in Java using Swing.
 *
 * Features:
 * - Two-player mode (Player X and Player O)
 * - Game board with 3x3 buttons
 * - Detects Win, Draw, or ongoing game
 * - Restart button to reset the game
 *
 * Complexity:
 * - Time: O(1) per move
 * - Space: O(1)
 *
 * Author: Pradyumn Pratap Singh (Strange)
 * For: Hacktoberfest / Mini Games in Java
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TicTacToeGUI extends JFrame implements ActionListener {

    private JButton[][] buttons = new JButton[3][3];
    private boolean isXTurn = true;
    private JLabel statusLabel;
    private JButton restartButton;

    public TicTacToeGUI() {
        setTitle("❌⭕ Tic Tac Toe Game");
        setSize(400, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));

        // --- Title ---
        JLabel title = new JLabel("Tic Tac Toe", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 22));
        title.setForeground(new Color(30, 144, 255));
        add(title, BorderLayout.NORTH);

        // --- Game Board ---
        JPanel boardPanel = new JPanel(new GridLayout(3, 3, 5, 5));
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                buttons[i][j] = new JButton("");
                buttons[i][j].setFont(new Font("Segoe UI", Font.BOLD, 40));
                buttons[i][j].setFocusPainted(false);
                buttons[i][j].addActionListener(this);
                boardPanel.add(buttons[i][j]);
            }
        }
        add(boardPanel, BorderLayout.CENTER);

        // --- Bottom Panel (Status + Restart) ---
        JPanel bottomPanel = new JPanel(new GridLayout(2,1));
        statusLabel = new JLabel("Player X's turn", SwingConstants.CENTER);
        statusLabel.setFont(new Font("Segoe UI", Font.PLAIN, 16));
        restartButton = new JButton("Restart Game");
        restartButton.addActionListener(e -> resetGame());
        bottomPanel.add(statusLabel);
        bottomPanel.add(restartButton);

        add(bottomPanel, BorderLayout.SOUTH);

        getContentPane().setBackground(new Color(245, 245, 245));
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        JButton clicked = (JButton) e.getSource();
        if (!clicked.getText().equals("")) return; // Ignore if already clicked

        clicked.setText(isXTurn ? "X" : "O");

        if (checkWin()) {
            statusLabel.setText("🎉 Player " + (isXTurn ? "X" : "O") + " wins!");
            disableButtons();
        } else if (isBoardFull()) {
            statusLabel.setText("🤝 It's a Draw!");
        } else {
            isXTurn = !isXTurn;
            statusLabel.setText("Player " + (isXTurn ? "X" : "O") + "'s turn");
        }
    }

    private boolean checkWin() {
        String player = isXTurn ? "X" : "O";

        // Check rows and columns
        for (int i = 0; i < 3; i++) {
            if (buttons[i][0].getText().equals(player) &&
                buttons[i][1].getText().equals(player) &&
                buttons[i][2].getText().equals(player))
                return true;

            if (buttons[0][i].getText().equals(player) &&
                buttons[1][i].getText().equals(player) &&
                buttons[2][i].getText().equals(player))
                return true;
        }

        // Check diagonals
        if (buttons[0][0].getText().equals(player) &&
            buttons[1][1].getText().equals(player) &&
            buttons[2][2].getText().equals(player))
            return true;

        if (buttons[0][2].getText().equals(player) &&
            buttons[1][1].getText().equals(player) &&
            buttons[2][0].getText().equals(player))
            return true;

        return false;
    }

    private boolean isBoardFull() {
        for (JButton[] row : buttons) {
            for (JButton btn : row) {
                if (btn.getText().equals("")) return false;
            }
        }
        return true;
    }

    private void disableButtons() {
        for (JButton[] row : buttons)
            for (JButton btn : row)
                btn.setEnabled(false);
    }

    private void resetGame() {
        for (JButton[] row : buttons)
            for (JButton btn : row) {
                btn.setText("");
                btn.setEnabled(true);
            }
        isXTurn = true;
        statusLabel.setText("Player X's turn");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(TicTacToeGUI::new);
    }
}
