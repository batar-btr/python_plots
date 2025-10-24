import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(100_000)
rw.fill_walk()

# Plot the points in the walk

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values,
           cmap=plt.cm.cool,
           c=range(rw.num_points),
           s=5,
           alpha=0.5,
           edgecolors='none')
ax.set_aspect('equal')

# Remove axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
