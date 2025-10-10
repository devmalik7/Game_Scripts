import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class RockPaperScissorsGUI extends JFrame implements ActionListener {

    private JLabel resultLabel;
    private JLabel computerChoiceLabel;
    private JButton rockButton, paperButton, scissorsButton;
    private String[] options = {"Rock", "Paper", "Scissors"};
    private Random random = new Random();

    public RockPaperScissorsGUI() {
        setTitle("🪨 Rock Paper Scissors");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Title
        JLabel title = new JLabel("🎮 Rock Paper Scissors", SwingConstants.CENTER);
        title.setFont(new Font("Arial", Font.BOLD, 20));
        add(title, BorderLayout.NORTH);

        // Buttons panel
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new FlowLayout());

        rockButton = new JButton("Rock 🪨");
        paperButton = new JButton("Paper 📄");
        scissorsButton = new JButton("Scissors ✂️");

        rockButton.addActionListener(this);
        paperButton.addActionListener(this);
        scissorsButton.addActionListener(this);

        buttonPanel.add(rockButton);
        buttonPanel.add(paperButton);
        buttonPanel.add(scissorsButton);

        add(buttonPanel, BorderLayout.CENTER);

        // Result label
        resultLabel = new JLabel("Choose your move!", SwingConstants.CENTER);
        resultLabel.setFont(new Font("Arial", Font.PLAIN, 16));
        add(resultLabel, BorderLayout.SOUTH);

        // Computer choice label
        computerChoiceLabel = new JLabel("", SwingConstants.CENTER);
        add(computerChoiceLabel, BorderLayout.AFTER_LAST_LINE);

        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String userChoice = "";
        if (e.getSource() == rockButton) userChoice = "Rock";
        else if (e.getSource() == paperButton) userChoice = "Paper";
        else if (e.getSource() == scissorsButton) userChoice = "Scissors";

        // Animate computer choice
        new Thread(() -> {
            try {
                for (int i = 0; i < 5; i++) {
                    String tempChoice = options[random.nextInt(3)];
                    computerChoiceLabel.setText("Computer is choosing: " + tempChoice);
                    Thread.sleep(200);
                }
                String computerChoice = options[random.nextInt(3)];
                computerChoiceLabel.setText("Computer chose: " + computerChoice);

                // Decide winner
                String winner = "";
                if (userChoice.equals(computerChoice)) winner = "It's a tie!";
                else if ((userChoice.equals("Rock") && computerChoice.equals("Scissors")) ||
                        (userChoice.equals("Paper") && computerChoice.equals("Rock")) ||
                        (userChoice.equals("Scissors") && computerChoice.equals("Paper"))) winner = "You win! 🎉";
                else winner = "You lose! 💀";

                resultLabel.setText(winner);

            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        }).start();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new RockPaperScissorsGUI());
    }
}
