const gridElement = document.getElementById("grid");
const startBtn = document.getElementById("startbtn");
const pauseBtn = document.getElementById("pausebtn");
const restartBtn = document.getElementById("restartbtn");
const scoreElement = document.getElementById("score");
const finalscoreElement = document.getElementById("finalscore");

const welcomeScreen = document.getElementById("welcomescreen");
const gameScreen = document.getElementById("gamescreen");
const gameoverScreen = document.getElementById("gameoverscreen");

let squares = [];
let currentSnake = [2, 1, 0];
let direction = 1;
const width = 10;
let appleIndex = 0;
let score = 0;
let intervalTime = 300;
let speed = 0.9;
let timerId;
let paused = false;
let started = false;

function createGrid() {
  gridElement.innerHTML = "";
  squares = [];
  for (let i = 0; i < width * width; i++) {
    const square = document.createElement("div");
    square.classList.add("square");
    gridElement.appendChild(square);
    squares.push(square);
  }
}

function startGame() {
  welcomeScreen.classList.add("hidden");
  gameoverScreen.classList.add("hidden");
  gameScreen.classList.remove("hidden");

  createGrid();
  currentSnake = [2, 1, 0];
  direction = 1;
  score = 0;
  intervalTime = 400;
  paused = false;
  started = true;
  scoreElement.textContent = `Score: ${score}`;
  pauseBtn.textContent = "Pause";

  squares.forEach((i) => i.classList.remove("snake", "apple"));
  currentSnake.forEach((i) => squares[i].classList.add("snake"));

  generateApple();

  clearInterval(timerId);
  timerId = setInterval(move, intervalTime);
}

function move() {
  if (paused) return;

  if (
    (currentSnake[0] + width >= width * width && direction === width) ||
    (currentSnake[0] % width === width - 1 && direction === 1) ||
    (currentSnake[0] % width === 0 && direction === -1) ||
    (currentSnake[0] - width < 0 && direction === -width) ||
    squares[currentSnake[0] + direction].classList.contains("snake")
  ) {
    clearInterval(timerId);
    gameOver();
    return;
  }

  const tail = currentSnake.pop();
  squares[tail].classList.remove("snake");
  currentSnake.unshift(currentSnake[0] + direction);

  if (squares[currentSnake[0]].classList.contains("apple")) {
    squares[currentSnake[0]].classList.remove("apple");
    squares[tail].classList.add("snake");
    currentSnake.push(tail);
    generateApple();
    score++;
    scoreElement.textContent = `Score: ${score}`;
    clearInterval(timerId);
    if (intervalTime > 200) {
      intervalTime = intervalTime * speed;
    }
    timerId = setInterval(move, intervalTime);
  }

  squares[currentSnake[0]].classList.add("snake");
}

function generateApple() {
  do {
    appleIndex = Math.floor(Math.random() * squares.length);
  } while (squares[appleIndex].classList.contains("snake"));
  squares[appleIndex].classList.add("apple");
}

function control(k) {
  if (!started || paused) return;
  if (k.key === "ArrowRight" && direction !== -1) direction = 1;
  else if (k.key === "ArrowUp" && direction !== width) direction = -width;
  else if (k.key === "ArrowLeft" && direction !== 1) direction = -1;
  else if (k.key === "ArrowDown" && direction !== -width) direction = +width;
}

document.addEventListener("keydown", control);

function stopGame() {
  if (!started) return;
  paused = !paused;
  pauseBtn.textContent = paused ? "Resume" : "Pause";
}

function gameOver() {
  started = false;
  gameScreen.classList.add("hidden");
  gameoverScreen.classList.remove("hidden");
  finalscoreElement.textContent = `Your score: ${score}`;
}

startBtn.addEventListener("click", startGame);
restartBtn.addEventListener("click", startGame);
pauseBtn.addEventListener("click", stopGame);
