from alignment import alignment_score
from mask_utils import polygon_to_mask

import numpy as np

# fake edge image

edges = np.zeros(
    (100,150),
    dtype=np.uint8
)

edges[20:50,60] = 255

polygon_pixels = np.array([
    [20,20],
    [120,20],
    [120,50],
    [20,50]
])

mask = polygon_to_mask(
    (100,150),
    polygon_pixels
)

score = alignment_score(
    edges,
    mask
)

print(
    "Alignment score:",
    score
)