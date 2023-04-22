import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
"""
# Fixing random state for reproducibility
np.random.seed(19680801)


def random_walk(num_steps, max_step=0.05):
    #Return a 3D random walk as (num_steps, 3) array.
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk


def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines


# Data: 40 random walks as (num_steps, 3) arrays
num_steps = 30
walks = [random_walk(num_steps) for index in range(2)]

# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Create lines initially without data
lines = [ax.plot([], [], [])[0] for _ in walks]

# Setting the axes properties
ax.set(xlim3d=(0, 1), xlabel='X')
ax.set(ylim3d=(0, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')

# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)

plt.show()"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Generate some data
theta = np.linspace(0, 2*np.pi, 100)
x1 = np.cos(theta)
y1 = np.sin(theta)
x2 = np.cos(theta + np.pi/4)
y2 = np.sin(theta + np.pi/4)

# Create a figure and an axes object
fig, ax = plt.subplots()

ax.set_xlim([min(x2) - 0.5, max(x2) + 0.5])
ax.set_ylim([min(y2) - 0.5, max(y2) + 0.5])

# Initialize the points
point1, = ax.plot([], [], 'o', color='red')
point2, = ax.plot([], [], 'o', color='blue')

# Define the animation function
def animate(i):
    # Update the positions of the points
    point1.set_data([x1[i], y1[i]])
    point2.set_data([x2[i], y2[i]])
    return point1, point2

# Create the animation object
ani = FuncAnimation(fig, animate, frames=len(theta), blit=True)

# Show the plot
plt.show()

