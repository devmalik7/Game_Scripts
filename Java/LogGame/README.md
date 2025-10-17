# 📝 Log Game

A simple **Java Swing** application that lets users create and manage a live log through an interactive GUI.  
You can add timestamped entries, insert separators, and clear all logs with a single click.

---

## 💡 Features

- 🕒 **Timestamped entries** — each log line records the current hour, minute, and second.
- ➕ **Add entries** — type a short message and press **Add Log Entry**.
- 🧹 **Clear log** — instantly clears all log text and resets the counter.
- 🔹 **Add separators** — insert visual separators between log sections.
- 🎨 **Simple GUI** — intuitive layout with tooltips for each button.

---

## 🧩 How It Works

When the program runs:
1. A window titled **“Mini Log”** opens.
2. Users can type into the text box at the bottom.
3. Three buttons are available:
   - **Clear Log** — clears all log entries.
   - **Add Log Entry** — adds a new line with a timestamp.
   - **Add Separator** — inserts a dashed separator line.
4. All entries appear in the center text area, with timestamps generated using `Calendar`.

---

## 💻 Code Overview

### Main Components
| Component | Description |
|------------|-------------|
| `JFrame` | Main application window |
| `JTextArea` | Displays the log content |
| `JTextField` | Allows user input for new entries |
| `JButton` | Controls (Clear, Add Entry, Add Separator) |
| `ActionListener` | Handles all button events |
| `Calendar` | Generates timestamps for each entry |

### Complexity
- **Time Complexity:** `O(1)` per operation  
- **Space Complexity:** `O(n)` where `n` = number of log entries

---

## 🚀 Running the Program

### 1. Compile
Open your terminal in the project directory and run:
```bash
javac logGame.java
