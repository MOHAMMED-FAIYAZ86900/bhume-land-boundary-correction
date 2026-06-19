from bhume import load, patch_for_plot
from bhume.geo import open_imagery

from src.edges import extract_edges

import matplotlib.pyplot as plt

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

imagery = open_imagery(
    "data/34855_vadnerbhairav_chandavad_nashik/imagery.tif"
)

row = village.plots.iloc[0]

geom = row["geometry"]

patch = patch_for_plot(
    imagery,
    geom
)

edges = extract_edges(
    patch.image
)

plt.imshow(
    edges,
    cmap="gray"
)

plt.axis("off")

plt.savefig(
    "real_edges.png",
    bbox_inches="tight"
)

print(
    "Saved real_edges.png"
)