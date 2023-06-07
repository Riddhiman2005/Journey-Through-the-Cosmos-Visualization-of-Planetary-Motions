
<!DOCTYPE html>
<html>
<head>
    <title>Solar System</title>
    <style>
        canvas {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <canvas id="canvas" width="800" height="600"></canvas>

    <script>
        // Get the canvas element
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');

        // Set up variables for each planet
        const sunRadius = 50;
        const planetData = [
            { name: 'Mercury', radius: 10, distance: 100, speed: 0.005, color: 'gray' },
            { name: 'Venus', radius: 15, distance: 150, speed: 0.004, color: 'orange' },
            { name: 'Earth', radius: 20, distance: 200, speed: 0.003, color: 'blue' },
            { name: 'Mars', radius: 18, distance: 250, speed: 0.002, color: 'red' },
            { name: 'Jupiter', radius: 30, distance: 350, speed: 0.001, color: 'brown' },
            { name: 'Saturn', radius: 28, distance: 450, speed: 0.0008, color: 'goldenrod' },
            { name: 'Uranus', radius: 25, distance: 550, speed: 0.0006, color: 'cyan' },
            { name: 'Neptune', radius: 23, distance: 650, speed: 0.0004, color: 'darkblue' }
        ];

        function draw() {
            // Clear the canvas
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Draw the Sun
            ctx.fillStyle = 'yellow';
            ctx.beginPath();
            ctx.arc(canvas.width / 2, canvas.height / 2, sunRadius, 0, 2 * Math.PI);
            ctx.fill();

            // Draw each planet
            for (let i = 0; i < planetData.length; i++) {
                const planet = planetData[i];
                const time = Date.now();
                const angle = (time * planet.speed) % (2 * Math.PI);
                const x = canvas.width / 2 + planet.distance * Math.cos(angle);
                const y = canvas.height / 2 + planet.distance * Math.sin(angle);

                ctx.fillStyle = planet.color;
                ctx.beginPath();
                ctx.arc(x, y, planet.radius, 0, 2 * Math.PI);
                ctx.fill();

                // Draw the orbit path
                ctx.strokeStyle = 'white';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.arc(canvas.width / 2, canvas.height / 2, planet.distance, 0, 2 * Math.PI);
                ctx.stroke();
            }

            // Request animation frame for smooth animation
            requestAnimationFrame(draw);
        }

        // Start the animation
        draw();
    </script>
</body>
</html>



