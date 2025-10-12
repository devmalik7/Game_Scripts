const coin = document.getElementById('coin');
const flipBtn = document.getElementById('flip-btn');

flipBtn.addEventListener('click', () => {
  coin.classList.add('flipping');
  coin.textContent = '?';

  setTimeout(() => {
    const result = Math.random() < 0.5 ? 'Heads' : 'Tails';
    coin.textContent = result;
    coin.classList.remove('flipping');
  }, 1000);
});
