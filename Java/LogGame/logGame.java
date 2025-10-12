/*
 * Log Game
 * A simple logging application with a GUI.
 * Users can add log entries, clear the log, and add separators.
 * Each log entry is timestamped. 
 * TimeComplexity: O(1) for each operation.
 * SpaceComplexity: O(n) where n is the number of log entries.
 */
import javax.swing.*;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Calendar;
public class logGame {
  static int count = 1;
  public static void main(String[] args){
    JFrame window = new JFrame("Mini Log");
    BorderLayout border = new BorderLayout();
    window.getContentPane().setLayout(border);
    window.setSize(400, 400);
    JButton button1 = new JButton("Clear Log");
    button1.setToolTipText("Click this to clear the log entries");
    JButton button2 = new JButton("Add Log Entry");
    button2.setToolTipText("Click this to add a log entry");
    JButton button3 = new JButton("Add Seperator");
    button3.setToolTipText("Click this to add a seperator");

    JPanel panel = new JPanel(new GridLayout(1, 4));
    JTextField input = new JTextField();
    input.setToolTipText("Input a short log entry");
    panel.add(input);
    panel.add(button1);
    panel.add(button2);
    panel.add(button3);
    JLabel label = new JLabel("My Awesome Log", SwingConstants.CENTER);
    JTextArea ta = new JTextArea();
    window.getContentPane().add(panel, BorderLayout.SOUTH);
    window.getContentPane().add(label, BorderLayout.NORTH);
    // window.getContentPane().add(button1, BorderLayout.WEST);
    // window.getContentPane().add(panel, BorderLayout.EAST);
    window.getContentPane().add(ta, BorderLayout.CENTER);
    window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    window.setVisible(true);
    
    

    //window.getContentPane().setLayout(new BorderLayout());
    window.getContentPane().setBackground(Color.lightGray);

    ActionListener buttonListener = new ActionListener() {
      @Override
      public void actionPerformed(ActionEvent e){
        if(e.getSource() == button1){
          ta.setText("");
          count = 1;
        }
        else if(e.getSource() == button2){
          Calendar c = Calendar.getInstance();
          int hour = c.get(Calendar.HOUR);
          int minute = c.get(Calendar.MINUTE);
          int second = c.get(Calendar.SECOND);
          String str = input.getText();
          String add = ("[" + hour + ":" + minute + ":" + second + "] log" + count + ": " + str + "\n");
          ta.append(add);
          input.setText("");
          count++;
        }
        else if(e.getSource() == button3){
          String add = "------------------\n";
          ta.append(add);
        }
        System.out.println("click");
      }
    };
    button1.addActionListener(buttonListener);
    button2.addActionListener(buttonListener);
    button3.addActionListener(buttonListener);
  }
}
