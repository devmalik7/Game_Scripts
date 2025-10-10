package Java.PongGameGUI;
/**
 * 🎮 Pong Game GUI
 *
 * A classic 2-player Pong game implemented using Java Swing.
 * Players control paddles to bounce the ball and score points.
 *
 * Features:
 * - Two-player mode (Left paddle: W/S, Right paddle: Up/Down arrows)
 * - Ball movement and collision detection
 * - Score tracking
 * - Simple restart functionality
 *
 * Complexity:
 * - Time: O(1) per frame
 * - Space: O(1) for ball and paddles
 *
 * Author: Pradyumn Pratap Singh (Strange)
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class PongGameGUI extends JPanel implements KeyListener, ActionListener {

    private int ballX = 250, ballY = 150, ballDX = 2, ballDY = 2, ballSize = 20;
    private int paddle1Y = 100, paddle2Y = 100, paddleWidth = 10, paddleHeight = 80;
    private int score1 = 0, score2 = 0;
    private Timer timer;

    public PongGameGUI() {
        JFrame frame = new JFrame("🎮 Pong Game");
        frame.setSize(500, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.addKeyListener(this);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);

        // Timer for ball movement (refresh every 10ms)
        timer = new Timer(10, this);
        timer.start();
    }

    // Paint the game components
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Background
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, getWidth(), getHeight());

        // Ball
        g.setColor(Color.WHITE);
        g.fillOval(ballX, ballY, ballSize, ballSize);

        // Paddles
        g.fillRect(10, paddle1Y, paddleWidth, paddleHeight);
        g.fillRect(getWidth() - 20, paddle2Y, paddleWidth, paddleHeight);

        // Scores
        g.setFont(new Font("Arial", Font.BOLD, 20));
        g.drawString("Player 1: " + score1, 50, 30);
        g.drawString("Player 2: " + score2, getWidth() - 150, 30);
    }

    // Move the ball and check collisions
    @Override
    public void actionPerformed(ActionEvent e) {
        ballX += ballDX;
        ballY += ballDY;

        // Bounce off top/bottom walls
        if (ballY <= 0 || ballY >= getHeight() - ballSize) ballDY = -ballDY;

        // Paddle collision (left paddle)
        if (ballX <= 20 && ballY + ballSize >= paddle1Y && ballY <= paddle1Y + paddleHeight) {
            ballDX = -ballDX;
        }

        // Paddle collision (right paddle)
        if (ballX + ballSize >= getWidth() - 20 && ballY + ballSize >= paddle2Y && ballY <= paddle2Y + paddleHeight) {
            ballDX = -ballDX;
        }

        // Score for Player 2
        if (ballX <= 0) {
            score2++;
            resetBall();
        }

        // Score for Player 1
        if (ballX >= getWidth() - ballSize) {
            score1++;
            resetBall();
        }

        repaint();
    }

    // Reset ball to center
    private void resetBall() {
        ballX = getWidth() / 2 - ballSize / 2;
        ballY = getHeight() / 2 - ballSize / 2;
        ballDX = -ballDX; // Change direction
        ballDY = 2;
    }

    // Key controls for paddles
    @Override
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();

        // Player 1 (W/S)
        if (key == KeyEvent.VK_W && paddle1Y > 0) paddle1Y -= 10;
        if (key == KeyEvent.VK_S && paddle1Y < getHeight() - paddleHeight) paddle1Y += 10;

        // Player 2 (Up/Down)
        if (key == KeyEvent.VK_UP && paddle2Y > 0) paddle2Y -= 10;
        if (key == KeyEvent.VK_DOWN && paddle2Y < getHeight() - paddleHeight) paddle2Y += 10;

        repaint();
    }

    @Override
    public void keyReleased(KeyEvent e) { }

    @Override
    public void keyTyped(KeyEvent e) { }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(PongGameGUI::new);
    }
}
