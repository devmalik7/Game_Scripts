const board = document.getElementById("game-board");
const level = localStorage.getItem("game-level");

const sizes = {
  easy: 2,
  medium: 4,
  hard: 6,
};

const gridSize = sizes[level];
const totalCards = gridSize * gridSize;
const symbols = [
  "assets/icon1.png",
  "assets/icon2.png",
  "assets/icon3.png",
  "assets/icon4.png",
  "assets/icon5.png",
  "assets/icon6.png",
  "assets/icon7.png",
  "assets/icon8.png",
  "assets/icon9.png",
  "assets/icon10.png",
  "assets/icon11.png",
  "assets/icon12.png",
  "assets/icon13.png",
  "assets/icon14.png",
  "assets/icon15.png",
  "assets/icon16.png",
  "assets/icon17.png",
  "assets/icon18.png",
  "assets/icon19.png",
  "assets/icon20.png",
  "assets/icon21.png",
  "assets/icon22.png",
  "assets/icon23.png",
  "assets/icon24.png",
  "assets/icon25.png",
  "assets/icon26.png",
  "assets/icon27.png",
];
let lockBoard = false;
let gameSymbols = [];
let checkedCards = [];
let matchedCards = [];

function shuffle(array) {
  return array.sort(() => 0.5 - Math.random());
}

function createCard(symbol, index) {
  const card = document.createElement("div");
  card.classList.add("card");
  card.dataset.symbol = symbol;
  card.dataset.index = index;
  const img = document.createElement("img");
  img.classList.add("card-img");
  img.src = " ";
  card.appendChild(img);
  card.addEventListener("click", () => checkCard(card));
  board.appendChild(card);
}

function checkCard(card) {
  if (
    lockBoard ||
    checkedCards.length === 2 ||
    matchedCards.includes(card.dataset.index)
  )
    return;

  card.classList.add("checked");
  const img = card.querySelector("img");
  img.src = card.dataset.symbol;
  checkedCards.push(card);

  if (checkedCards.length === 2) {
    lockBoard = true;
    setTimeout(checkMatch, 1000);
  }
}

function checkMatch() {
  const [card1, card2] = checkedCards;
  if (card1.dataset.symbol === card2.dataset.symbol) {
    matchedCards.push(card1.dataset.index, card2.dataset.index);
    checkedCards = [];
    lockBoard = false;
  } else {
    setTimeout(() => {
      card1.classList.remove("checked");
      card2.classList.remove("checked");
      card1.querySelector("img").src = " ";
      card2.querySelector("img").src = " ";
      checkedCards = [];
      lockBoard = false;
    }, 500);
  }
  if (matchedCards.length === gameSymbols.length) {
    document.getElementById("win-message").style.display = "block";
  }
}

function startGame() {
  board.innerHTML = "";
  matchedCards = [];
  checkedCards = [];
  board.style.gridTemplateColumns = `repeat(${gridSize}, 100px)`;
  document.getElementById("win-message").style.display = "none";

  const selectedSymbols = shuffle(symbols).slice(0, totalCards / 2);
  gameSymbols = shuffle([...selectedSymbols, ...selectedSymbols]);
  gameSymbols.forEach((symbol, index) => createCard(symbol, index));
}

function restartGame() {
  startGame();
}

document.addEventListener("DOMContentLoaded", () => {
  startGame();
});
