from mask_utils import polygon_to_mask

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# Fake polygon for testing
# ---------------------------------

polygon_pixels = np.array([
    [20, 20],
    [120, 20],
    [120, 50],
    [20, 50]
])

# ---------------------------------
# Create mask
# ---------------------------------

mask = polygon_to_mask(
    (100, 150),
    polygon_pixels
)

# ---------------------------------
# Save image
# ---------------------------------

plt.figure(figsize=(6,4))
plt.imshow(mask, cmap="gray")
plt.axis("off")

plt.savefig(
    "plot1145_mask.png",
    bbox_inches="tight"
)

print(
    "Saved plot1145_mask.png"
)