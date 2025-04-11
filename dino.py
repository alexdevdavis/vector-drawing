import matplotlib.pyplot as plt
import numpy as np
import matplotlib.spines as msp
import matplotlib.path as mpath

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


origin_x_spine = msp.Spine(ax, 'bottom', mpath.Path([[0.0,0.0], [1.0, 0.0]])) 
origin_x_spine.set_linewidth(2)
ax.spines['origin_x'] = origin_x_spine
ax.add_patch(origin_x_spine)

origin_y_spine = msp.Spine(ax, 'left', mpath.Path([[0.0,0.0], [0.0, 0.0]])) 
origin_y_spine.set_linewidth(2)
ax.spines['origin_y'] = origin_y_spine
ax.add_patch(origin_y_spine)


min_x = min(dino_x) if dino_x else -6
min_y = min(dino_y) if dino_y else -6
max_x = max(dino_x) if dino_x else 6
max_y = max(dino_y) if dino_y else 6

padding = 1
ax.set_xlim((min_x - padding, max_x + padding))
ax.set_ylim((min_y - padding, max_y + padding))

ax.set_xlabel('x', loc='right', labelpad=2)
ax.set_ylabel('y', loc='top', rotation=0, labelpad=1)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.plot(dino_x, dino_y, 'ro-')

ax.set_aspect('equal', adjustable='box')

plt.title('Dino Plot')

plt.grid(True)
fig.savefig('dino_plot.png')
plt.show()

