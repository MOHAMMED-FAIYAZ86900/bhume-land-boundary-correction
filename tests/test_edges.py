from bhume import load, patch_for_plot
from bhume.geo import open_imagery

from src.alignment import extract_edges

import matplotlib.pyplot as plt

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

edges = extract_edges(
    patch.image
)

plt.figure(figsize=(8,6))
plt.imshow(edges, cmap="gray")
plt.axis("off")
plt.savefig("edges_plot1145.png", bbox_inches="tight")
print("Saved edges_plot1145.png")