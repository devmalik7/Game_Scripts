/**
 * 🎮 Brick Breaker GUI Game
 *
 * Classic Brick Breaker game using Java Swing.
 * Player controls a paddle to bounce the ball and break bricks.
 *
 * Features:
 * - Paddle moves left/right using arrow keys
 * - Ball bounces off walls, paddle, and bricks
 * - Score tracking
 * - Game over and restart functionality
 *
 * Complexity:
 * - Time: O(1) per frame
 * - Space: O(n*m) for brick grid
 *
 * Author: Pradyumn Pratap Singh (Strange)
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class BrickBreakerGUI extends JPanel implements KeyListener, ActionListener {

    private Timer timer;
    private int delay = 8; // timer delay

    private int paddleX = 310; // paddle position
    private int paddleWidth = 100;

    private int ballX = 120, ballY = 350, ballDX = -2, ballDY = -3, ballSize = 20;

    private int score = 0;
    private int totalBricks = 21;

    private int brickRow = 3;
    private int brickCol = 7;
    private int brickWidth = 60;
    private int brickHeight = 20;
    private int[][] bricks = new int[brickRow][brickCol];

    public BrickBreakerGUI() {
        // Initialize bricks
        for (int i = 0; i < brickRow; i++) {
            for (int j = 0; j < brickCol; j++) {
                bricks[i][j] = 1; // brick is visible
            }
        }

        addKeyListener(this);
        setFocusable(true);
        setFocusTraversalKeysEnabled(false);

        timer = new Timer(delay, this);
        timer.start();
    }

    // Draw game components
    @Override
    public void paint(Graphics g) {
        // Background
        g.setColor(Color.BLACK);
        g.fillRect(1, 1, 700, 600);

        // Draw bricks
        for (int i = 0; i < brickRow; i++) {
            for (int j = 0; j < brickCol; j++) {
                if (bricks[i][j] == 1) {
                    g.setColor(Color.RED);
                    g.fillRect(j * brickWidth + 80, i * brickHeight + 50, brickWidth, brickHeight);
                    g.setColor(Color.BLACK);
                    g.drawRect(j * brickWidth + 80, i * brickHeight + 50, brickWidth, brickHeight);
                }
            }
        }

        // Paddle
        g.setColor(Color.GREEN);
        g.fillRect(paddleX, 500, paddleWidth, 10);

        // Ball
        g.setColor(Color.YELLOW);
        g.fillOval(ballX, ballY, ballSize, ballSize);

        // Score
        g.setColor(Color.WHITE);
        g.setFont(new Font("Arial", Font.BOLD, 20));
        g.drawString("Score: " + score, 590, 30);

        // Game Over
        if (ballY > 570) {
            g.setColor(Color.RED);
            g.setFont(new Font("Arial", Font.BOLD, 30));
            g.drawString("Game Over! Score: " + score, 180, 300);
            timer.stop();
        }

        // Win
        if (totalBricks <= 0) {
            g.setColor(Color.GREEN);
            g.setFont(new Font("Arial", Font.BOLD, 30));
            g.drawString("You Won! Score: " + score, 180, 300);
            timer.stop();
        }

        g.dispose();
    }

    // Game loop
    @Override
    public void actionPerformed(ActionEvent e) {
        timer.start();

        // Ball-paddle collision
        if (new Rectangle(ballX, ballY, ballSize, ballSize)
                .intersects(new Rectangle(paddleX, 500, paddleWidth, 10))) {
            ballDY = -ballDY;
        }

        // Ball-brick collision
        A: for (int i = 0; i < brickRow; i++) {
            for (int j = 0; j < brickCol; j++) {
                if (bricks[i][j] == 1) {
                    int brickX = j * brickWidth + 80;
                    int brickY = i * brickHeight + 50;

                    Rectangle brickRect = new Rectangle(brickX, brickY, brickWidth, brickHeight);
                    Rectangle ballRect = new Rectangle(ballX, ballY, ballSize, ballSize);

                    if (ballRect.intersects(brickRect)) {
                        bricks[i][j] = 0;
                        totalBricks--;
                        score += 5;

                        // Change ball direction
                        if (ballX + ballSize - 1 <= brickRect.x || ballX + 1 >= brickRect.x + brickRect.width) {
                            ballDX = -ballDX;
                        } else {
                            ballDY = -ballDY;
                        }
                        break A;
                    }
                }
            }
        }

        // Move ball
        ballX += ballDX;
        ballY += ballDY;

        // Ball-wall collision
        if (ballX < 0) ballDX = -ballDX;
        if (ballY < 0) ballDY = -ballDY;
        if (ballX > 680) ballDX = -ballDX;

        repaint();
    }

    // Paddle movement
    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
            paddleX += 20;
            if (paddleX > 600) paddleX = 600;
        }
        if (e.getKeyCode() == KeyEvent.VK_LEFT) {
            paddleX -= 20;
            if (paddleX < 10) paddleX = 10;
        }
        repaint();
    }

    @Override
    public void keyReleased(KeyEvent e) { }

    @Override
    public void keyTyped(KeyEvent e) { }

    public static void main(String[] args) {
        JFrame frame = new JFrame();
        BrickBreakerGUI game = new BrickBreakerGUI();
        frame.setBounds(10, 10, 700, 600);
        frame.setTitle("🎮 Brick Breaker");
        frame.setResizable(false);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(game);
    }
}
