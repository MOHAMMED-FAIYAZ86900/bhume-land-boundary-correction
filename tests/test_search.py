from search import find_best_shift
import numpy as np

edges = np.zeros(
    (100,150),
    dtype=np.uint8
)

# vertical edge
edges[20:50,80] = 255

polygon_pixels = np.array([
    [70,20],
    [75,20],
    [75,50],
    [70,50]
])

dx, dy, score = find_best_shift(
    edges,
    polygon_pixels,
    (100,150)
)

print("dx =", dx)
print("dy =", dy)
print("score =", score)