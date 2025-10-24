const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const resetButton = document.getElementById('resetButton');

const GRAVITY = 0.5;
let player;
let platforms = [];
let goal;
let keys = {
    right: false,
    left: false,
    up: false
};
let gameActive = true;
let winMessage = "You Win!";

// Player Class
class Player {
    constructor() {
        this.position = { x: 100, y: 400 };
        this.velocity = { x: 0, y: 0 };
        this.width = 30;
        this.height = 30;
        this.onGround = false;
    }

    draw() {
        ctx.fillStyle = '#4CAF50';
        ctx.fillRect(this.position.x, this.position.y, this.width, this.height);
    }

    update() {
        this.draw();
        this.position.x += this.velocity.x;
        this.position.y += this.velocity.y;

        // Apply gravity if not at bottom of canvas
        if (this.position.y + this.height + this.velocity.y < canvas.height) {
            this.velocity.y += GRAVITY;
            this.onGround = false;
        } else {
            this.velocity.y = 0;
            this.position.y = canvas.height - this.height;
            this.onGround = true;
        }

        // --- NEW ---
        // Restart if player hits horizontal boundaries
        if (this.position.x < 0 || this.position.x + this.width > canvas.width) {
            init(); 
        }

        // Restart if player falls off bottom
        if (this.position.y > canvas.height) {
            init();
        }
    }
}

// Platform Class
class Platform {
    constructor(x, y, width, height) {
        this.position = { x, y };
        this.width = width;
        this.height = height;
    }

    draw() {
        ctx.fillStyle = '#8B4513'; // Brown color for platforms
        ctx.fillRect(this.position.x, this.position.y, this.width, this.height);
    }
}

// Goal Class
class Goal {
    constructor(x, y, width, height) {
        this.position = { x, y };
        this.width = width;
        this.height = height;
    }

    draw() {
        ctx.fillStyle = '#FFD700'; // Gold color for the goal
        ctx.fillRect(this.position.x, this.position.y, this.width, this.height);
    }
}

// Initialize game elements
function init() {
    gameActive = true;
    player = new Player();
    platforms = [
        new Platform(0, 550, 300, 50),
        new Platform(400, 450, 200, 50),
        new Platform(650, 350, 150, 50),
        new Platform(400, 250, 100, 50)
    ];
    goal = new Goal(425, 200, 50, 50); // Goal on the top platform
}

// Main animation loop
function animate() {
    if (!gameActive) {
        // Display win message
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.font = '60px Arial';
        ctx.fillStyle = '#FFD700';
        ctx.textAlign = 'center';
        ctx.fillText(winMessage, canvas.width / 2, canvas.height / 2);
        return;
    }

    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw goal
    goal.draw();

    // Draw platforms
    platforms.forEach(platform => {
        platform.draw();
    });

    // Update player
    player.update();

    // Player movement (boundary checks moved to player.update)
    if (keys.left) {
        player.velocity.x = -5;
    } else if (keys.right) {
        player.velocity.x = 5;
    } else {
        player.velocity.x = 0;
    }

    // Platform collision detection
    platforms.forEach(platform => {
        // Check for collision on top of the platform
        if (
            player.position.y + player.height <= platform.position.y &&
            player.position.y + player.height + player.velocity.y >= platform.position.y &&
            player.position.x + player.width >= platform.position.x &&
            player.position.x <= platform.position.x + platform.width
        ) {
            player.velocity.y = 0;
            player.position.y = platform.position.y - player.height;
            player.onGround = true;
        }
    });

    // Goal collision detection
    if (
        player.position.x < goal.position.x + goal.width &&
        player.position.x + player.width > goal.position.x &&
        player.position.y < goal.position.y + goal.height &&
        player.position.y + player.height > goal.position.y
    ) {
        gameActive = false; // Stop the game
    }
}

// Event Listeners
function handleKeyDown({ keyCode }) {
    switch (keyCode) {
        case 37: // Left Arrow
        case 65: // A
            keys.left = true;
            break;
        case 39: // Right Arrow
        case 68: // D
            keys.right = true;
            break;
        case 32: // Spacebar
        case 87: // W
            if (player.onGround) {
                player.velocity.y = -12; // Jump height
                player.onGround = false;
            }
            break;
    }
}

function handleKeyUp({ keyCode }) {
    switch (keyCode) {
        case 37: // Left Arrow
        case 65: // A
            keys.left = false;
            break;
        case 39: // Right Arrow
        case 68: // D
            keys.right = false;
            break;
    }
}

window.addEventListener('keydown', handleKeyDown);
window.addEventListener('keyup', handleKeyUp);

// --- UPDATED ---
// Reset button listener logic fixed
resetButton.addEventListener('click', () => {
    const wasGameStopped = !gameActive;
    init(); // Resets gameActive to true
    if (wasGameStopped) {
        animate(); // Manually restart the animation loop if it was stopped (on win screen)
    }
});

// Start the game
init();
animate();