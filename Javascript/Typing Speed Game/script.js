const words = [
  "code",
  "bug",
  "loop",
  "data",
  "html",
  "object",
  "method",
  "compile",
  "boolean",
  "library",
  "algorithm",
  "interface",
  "exception",
  "recursion",
  "prototype",
];

const welcomeScreen = document.getElementById("welcomescreen");
const gameScreen = document.getElementById("gamescreen");
const wordsContainer = document.getElementById("wordscontainer");
const input = document.getElementById("input");
const scoreElement = document.getElementById("score");
const statusElement = document.getElementById("msg");

const startBtn = document.getElementById("startbtn");
const pauseBtn = document.getElementById("pausebtn");
const restartBtn = document.getElementById("restartbtn");

const easyBtn = document.getElementById("easyBtn");
const mediumBtn = document.getElementById("mediumBtn");
const hardBtn = document.getElementById("hardBtn");

let score = 0;
let activeWords = [];
let gameInterval;
let spawnInterval;
let paused = false;
let running = false;
let difficulty = "medium";
let moveSpeed = 50;
let spawnRate = 2000;
let scorePerWord = 2; // default for medium

// Difficulty setup (speed + spawn rate + points)
function setDifficulty(level) {
  difficulty = level;

  switch (level) {
    case "easy":
      moveSpeed = 75; // slower falling
      spawnRate = 2500; // fewer words
      scorePerWord = 1;
      break;
    case "medium":
      moveSpeed = 50;
      spawnRate = 2000;
      scorePerWord = 2;
      break;
    case "hard":
      moveSpeed = 25; // faster falling
      spawnRate = 1200; // more words
      scorePerWord = 3;
      break;
  }

  statusElement.textContent = `Difficulty: ${level.toUpperCase()}`;

  // ✅ Restart intervals if game already running
  if (running && !paused) {
    clearInterval(gameInterval);
    clearInterval(spawnInterval);
    gameInterval = setInterval(moveWords, moveSpeed);
    spawnInterval = setInterval(generateWord, spawnRate);
  }

  // ✅ Highlight selected button
  highlightDifficulty(level);
}

// Highlight active difficulty button
function highlightDifficulty(level) {
  [easyBtn, mediumBtn, hardBtn].forEach((btn) =>
    btn.classList.remove("active")
  );
  if (level === "easy") easyBtn.classList.add("active");
  if (level === "medium") mediumBtn.classList.add("active");
  if (level === "hard") hardBtn.classList.add("active");
}

// Difficulty buttons
easyBtn.addEventListener("click", () => setDifficulty("easy"));
mediumBtn.addEventListener("click", () => setDifficulty("medium"));
hardBtn.addEventListener("click", () => setDifficulty("hard"));

function generateWord() {
  if (!running || paused) return;

  const word = document.createElement("div");
  word.classList.add("word");
  word.textContent = words[Math.floor(Math.random() * words.length)];

  word.style.visibility = "hidden";
  wordsContainer.appendChild(word);
  const wordWidth = word.offsetWidth || 60;
  wordsContainer.removeChild(word);

  const maxLeft = wordsContainer.offsetWidth - wordWidth;
  const left = Math.random() * maxLeft;

  word.style.left = left + "px";
  word.style.top = "10px";
  word.style.visibility = "visible";

  wordsContainer.appendChild(word);
  activeWords.push(word);
}

function moveWords() {
  if (!running || paused) return;

  activeWords.forEach((word, i) => {
    let top = parseInt(word.style.top) || 10;
    top += 2;
    word.style.top = top + "px";

    if (top >= 280) {
      stopGame();
    }
  });
}

input.addEventListener("input", () => {
  const data = input.value.trim();
  activeWords.forEach((word, i) => {
    if (word.textContent === data) {
      score += scorePerWord; // ✅ Add points based on difficulty
      scoreElement.textContent = score;
      wordsContainer.removeChild(word);
      activeWords.splice(i, 1);
      input.value = "";
    }
  });
});

function startGame() {
  clearInterval(gameInterval);
  clearInterval(spawnInterval);

  score = 0;
  scoreElement.textContent = score;
  statusElement.textContent = "Game On!";
  input.disabled = false;
  input.value = "";
  input.focus();

  activeWords.forEach((w) => w.remove());
  activeWords = [];

  running = true;
  paused = false;
  pauseBtn.textContent = "Pause";

  // ✅ Use current difficulty settings
  gameInterval = setInterval(moveWords, moveSpeed);
  spawnInterval = setInterval(generateWord, spawnRate);
}

function pause() {
  if (!running) return;
  paused = !paused;
  statusElement.textContent = paused ? "Paused" : "Game On!";
  pauseBtn.textContent = paused ? "Resume" : "Pause";
}

function restart() {
  startGame();
}

function stopGame() {
  clearInterval(gameInterval);
  clearInterval(spawnInterval);
  statusElement.textContent = "Game Over!";
  input.disabled = true;
  running = false;
}

startBtn.addEventListener("click", () => {
  welcomeScreen.classList.add("hidden");
  gameScreen.classList.remove("hidden");
  startGame();
});

pauseBtn.addEventListener("click", pause);
restartBtn.addEventListener("click", restart);

highlightDifficulty("medium");
