/**
 * 🎮 TicTacToeGUI.java
 *
 * A simple GUI-based Tic Tac Toe game in Java using Swing.
 *
 * New Feature:
 * ✅ Added scoreboard tracking X wins, O wins, and Draws across rounds
 *
 * Author: Pradyumn Pratap Singh (Strange)
 * Enhanced by: Sakshi (Hacktoberfest Contribution)
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TicTacToeGUI extends JFrame implements ActionListener {

    private JButton[][] buttons = new JButton[3][3];
    private boolean isXTurn = true;
    private JLabel statusLabel, scoreLabel;
    private JButton restartButton;

    private int xWins = 0, oWins = 0, draws = 0;

    public TicTacToeGUI() {
        setTitle("❌⭕ Tic Tac Toe Game");
        setSize(400, 520);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));

        JLabel title = new JLabel("Tic Tac Toe", SwingConstants.CENTER);
        title.setFont(new Font("Segoe UI", Font.BOLD, 22));
        title.setForeground(new Color(30, 144, 255));
        add(title, BorderLayout.NORTH);

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

        JPanel bottomPanel = new JPanel(new GridLayout(3, 1));
        statusLabel = new JLabel("Player X's turn", SwingConstants.CENTER);
        statusLabel.setFont(new Font("Segoe UI", Font.PLAIN, 16));

        scoreLabel = new JLabel("Scoreboard → X: 0 | O: 0 | Draws: 0", SwingConstants.CENTER);
        scoreLabel.setFont(new Font("Segoe UI", Font.ITALIC, 14));
        scoreLabel.setForeground(new Color(80, 80, 80));

        restartButton = new JButton("Restart Game");
        restartButton.addActionListener(e -> resetGame());

        bottomPanel.add(statusLabel);
        bottomPanel.add(scoreLabel);
        bottomPanel.add(restartButton);

        add(bottomPanel, BorderLayout.SOUTH);

        getContentPane().setBackground(new Color(245, 245, 245));
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        JButton clicked = (JButton) e.getSource();
        if (!clicked.getText().equals("")) return;

        clicked.setText(isXTurn ? "X" : "O");

        if (checkWin()) {
            if (isXTurn) xWins++; else oWins++;
            statusLabel.setText("🎉 Player " + (isXTurn ? "X" : "O") + " wins!");
            disableButtons();
        } else if (isBoardFull()) {
            draws++;
            statusLabel.setText("🤝 It's a Draw!");
        } else {
            isXTurn = !isXTurn;
            statusLabel.setText("Player " + (isXTurn ? "X" : "O") + "'s turn");
        }

        scoreLabel.setText("Scoreboard → X: " + xWins + " | O: " + oWins + " | Draws: " + draws);
    }

    private boolean checkWin() {
        String player = isXTurn ? "X" : "O";

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
        for (JButton[] row : buttons)
            for (JButton btn : row)
                if (btn.getText().equals("")) return false;
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
