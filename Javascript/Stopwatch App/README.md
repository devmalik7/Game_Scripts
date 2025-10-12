# Beautiful Stopwatch App

A simple yet elegant web-based stopwatch application with start, stop, and reset functionality.

## Features

- Clean and modern UI with gradient backgrounds and glassmorphism effects
- Start, stop, and reset controls
- Millisecond precision timing
- Responsive design that works on all devices
- Smooth animations and transitions

## How to Use

1. Click the **Start** button to begin timing
2. Click the **Stop** button to pause the timer
3. Click the **Reset** button to reset the timer to zero

## Files

- `index.html` - Main HTML structure
- `style.css` - Styling and visual design
- `script.js` - Stopwatch functionality implementation

## Implementation Details

The stopwatch is implemented using vanilla JavaScript with a class-based approach for clean organization. It uses `setInterval` for updating the display every 10 milliseconds (for smooth millisecond counting) and properly manages the timing intervals to prevent memory leaks.

The UI features:
- Glassmorphism design with frosted glass effect
- Gradient color scheme
- Responsive button states with hover and active effects
- Disabled states for appropriate buttons
- Smooth animations and transitions

## Browser Support

Works in all modern browsers that support ES6 JavaScript features.