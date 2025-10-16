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

let score = 0;
let activeWords = [];
let gameInterval;
let spawnInterval;
let paused = false;
let running = false;

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
      score++;
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

  gameInterval = setInterval(moveWords, 50);
  spawnInterval = setInterval(generateWord, 2000);
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
