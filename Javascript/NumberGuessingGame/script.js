let targetNumber;
let attempts = 0;

function initGame() {
  targetNumber = Math.floor(Math.random() * 100) + 1;
  attempts = 0;
  document.getElementById("guessInput").value = "";
  document.getElementById("hint").textContent = "";
  document.getElementById("attempts").textContent = "";
  document.getElementById("guessInput").disabled = false;
  document.getElementById("guessButton").disabled = false;
}

function makeGuess() {
  const guessInput = document.getElementById("guessInput");
  const guess = parseInt(guessInput.value);

  if (isNaN(guess) || guess < 1 || guess > 100) {
    document.getElementById("hint").textContent = "Please enter a valid number between 1 and 100.";
    return;
  }

  attempts++;

  if (guess === targetNumber) {
    document.getElementById(
      "hint"
    ).textContent = `Congratulations! You guessed the number ${targetNumber} in ${attempts} attempts.`;
    document.getElementById("guessInput").disabled = true;
    document.getElementById("guessButton").disabled = true;
  } else if (guess < targetNumber) {
    document.getElementById("hint").textContent = "Too low! Try a higher number.";
  } else {
    document.getElementById("hint").textContent = "Too high! Try a lower number.";
  }

  document.getElementById("attempts").textContent = `Attempts: ${attempts}`;
  guessInput.value = "";
}

document.getElementById("guessButton").addEventListener("click", makeGuess);
document.getElementById("resetButton").addEventListener("click", initGame);
document.getElementById("guessInput").addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    makeGuess();
  }
});

// Initialize the game on load
initGame();
