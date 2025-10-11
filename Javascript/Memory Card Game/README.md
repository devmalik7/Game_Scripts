# 🧠 Memory Card Game

A responsive, difficulty-based memory card game built with HTML, CSS, and JavaScript. Players flip cards to find matching pairs of popular app icons. The game includes multiple difficulty levels, dynamic grid generation, image-based cards, and a win message when all pairs are matched.

---

## 🚀 Features

- 🎮 Three difficulty levels: Easy (2×2), Medium (4×4), Hard (6×6)
- 🖼️ Real app icons as card faces
- 🔄 Dynamic grid layout based on selected level
- ✅ Match detection and flip-back logic
- 🔒 Board lock during mismatch delay to prevent glitches
- 🎉 Win message when all pairs are matched
- 🔁 Restart button to replay instantly

---


---

## 🛠 Setup Instructions

1. Clone or download the repository.
2. Open `index.html` in your browser to start the game.
3. Select a difficulty level -> play!

---

## 🧩 How It Works

- `index.html` sets the difficulty level via `localStorage`.
- `game.html` reads the level and builds a grid of cards.
- Each card contains an `<img>` element whose `src` is set dynamically on flip.
- Matched cards stay revealed; mismatched ones flip back after a delay.
- When all pairs are matched, a win message appears.

---

## 🧪 Edge Case Handling

- Prevents flipping more than 2 cards at once.
- Locks the board during mismatch delay.
- Handles fast clicks and double-clicks gracefully.

---

## 📸 Credits

Icons used in this game are sourced from:
- [Icons8](https://icons8.com/)

---

## 📄 License

This project is for educational and personal use. Please respect trademark guidelines when using real app logos.

