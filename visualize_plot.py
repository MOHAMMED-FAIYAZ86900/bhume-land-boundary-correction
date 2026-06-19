from bhume import load, patch_for_plot
from bhume.geo import open_imagery
import matplotlib.pyplot as plt
import numpy as np

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

src = open_imagery(
    "data/34855_vadnerbhairav_chandavad_nashik/imagery.tif"
)

plot = village.plot("1145")

patch = patch_for_plot(
    src,
    plot
)

img = patch.image

plt.figure(figsize=(10,6))
plt.imshow(img)

plt.title("Plot 1145 Patch")
plt.axis("off")

plt.savefig(
    "plot1145_overlay.png",
    bbox_inches="tight"
)

print(
    "Saved plot1145_overlay.png"
)