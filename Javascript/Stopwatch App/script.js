class Stopwatch {
    constructor() {
        this.startTime = 0;
        this.elapsedTime = 0;
        this.timerInterval = null;
        this.isRunning = false;
        
        // DOM elements
        this.minutesElement = document.getElementById('minutes');
        this.secondsElement = document.getElementById('seconds');
        this.millisecondsElement = document.getElementById('milliseconds');
        this.startBtn = document.getElementById('startBtn');
        this.stopBtn = document.getElementById('stopBtn');
        this.resetBtn = document.getElementById('resetBtn');
        
        // Bind event listeners
        this.startBtn.addEventListener('click', () => this.start());
        this.stopBtn.addEventListener('click', () => this.stop());
        this.resetBtn.addEventListener('click', () => this.reset());
    }
    
    start() {
        if (!this.isRunning) {
            this.startTime = Date.now() - this.elapsedTime;
            this.timerInterval = setInterval(() => this.updateTime(), 10);
            this.isRunning = true;
            
            // Update button states
            this.startBtn.disabled = true;
            this.stopBtn.disabled = false;
        }
    }
    
    stop() {
        if (this.isRunning) {
            clearInterval(this.timerInterval);
            this.isRunning = false;
            
            // Update button states
            this.startBtn.disabled = false;
            this.stopBtn.disabled = true;
        }
    }
    
    reset() {
        this.stop();
        this.elapsedTime = 0;
        this.updateDisplay();
        
        // Update button states
        this.startBtn.disabled = false;
        this.stopBtn.disabled = true;
    }
    
    updateTime() {
        this.elapsedTime = Date.now() - this.startTime;
        this.updateDisplay();
    }
    
    updateDisplay() {
        const totalMilliseconds = this.elapsedTime;
        const minutes = Math.floor(totalMilliseconds / 60000);
        const seconds = Math.floor((totalMilliseconds % 60000) / 1000);
        const milliseconds = Math.floor((totalMilliseconds % 1000) / 10);
        
        this.minutesElement.textContent = this.padNumber(minutes);
        this.secondsElement.textContent = this.padNumber(seconds);
        this.millisecondsElement.textContent = this.padNumber(milliseconds);
    }
    
    padNumber(number) {
        return number.toString().padStart(2, '0');
    }
}

// Initialize the stopwatch when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new Stopwatch();
});