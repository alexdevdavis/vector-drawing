import matplotlib.pyplot as plt
import numpy as np

dino_vectors = [
    np.array([6, 4]),
    np.array([3, 2]),
    np.array([1, 2]),
    np.array([-1, 5]),
    np.array([-1, 5]),
    np.array([-2, 5]),
    np.array([-3, 4]),
    np.array([-4, 4]),
    np.array([-5, 3]),
    np.array([-5, 2]),
    np.array([-2, 2]),
    np.array([-5, 1]),
    np.array([-4, 0]),
    np.array([-2, 1]),
    np.array([-1, 0]),
    np.array([0, -3]),
    np.array([-1, -4]),
    np.array([1, -4]),
    np.array([2, -3]),
    np.array([1, -2]),
    np.array([3, -1]),
    np.array([5, 1]),
    np.array([6, 4]),
]

dino_x = [vector[0] for vector in dino_vectors]
dino_y = [vector[1] for vector in dino_vectors]

fig, ax = plt.subplots()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

min_x = min(dino_x) if dino_x else -6
min_y = min(dino_y) if dino_y else -6
max_x = max(dino_x) if dino_x else 6
max_y = max(dino_y) if dino_y else 6

padding = 1
ax.set_xlim((min_x - padding, max_x + padding))
ax.set_ylim((min_y - padding, max_y + padding))

ax.set_xlabel('x', loc='right')
ax.set_ylabel('y', loc='top', rotation=0)


ax.plot(dino_x, dino_y, 'ro-')

ax.set_aspect('equal', adjustable='box')

plt.title('Dino Plot')

plt.grid(True)
fig.savefig('dino_plot.png')
plt.show()

