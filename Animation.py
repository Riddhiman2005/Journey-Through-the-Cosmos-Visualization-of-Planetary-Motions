
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Setting up the figure and axis

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))
ax.set_axis_off()

# Creation of  the sun
sun = plt.Circle((0, 0), 0.1, color='yellow')
ax.add_artist(sun)

# Creating the Earth's orbit

orbit = plt.Circle((0, 0), 1, color='blue', fill=False)
ax.add_artist(orbit)

# Creation of the Earth
earth, = ax.plot([], [], 'o', color='green')

# Set up animation parameters
frames = 360  # Number of frames
angle = np.linspace(0, 2 * np.pi, frames)  # Angle for each frame
x = np.cos(angle)  # x-coordinates of Earth's position
y = np.sin(angle)  # y-coordinates of Earth's position

# Update function for animation
def update(frame):
    earth.set_data([x[frame]], [y[frame]])
    return earth,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Save the animation as a GIF using the Pillow writer
ani.save('earth_orbit.gif', writer='pillow')

print("Animation saved as 'earth_orbit.gif'.")
