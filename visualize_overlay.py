from bhume import load, patch_for_plot
from bhume.geo import (
    open_imagery,
    lonlat_to_pixel,
)

import matplotlib.pyplot as plt
import numpy as np

VILLAGE_DIR = (
    "data/34855_vadnerbhairav_chandavad_nashik"
)

PLOT_ID = "1145"

# --------------------------------
# Load data
# --------------------------------

village = load(VILLAGE_DIR)

imagery = open_imagery(
    f"{VILLAGE_DIR}/imagery.tif"
)

geom = village.plot(PLOT_ID)

patch = patch_for_plot(
    imagery,
    geom
)

img = patch.image

# --------------------------------
# Display patch
# --------------------------------

fig, ax = plt.subplots(
    figsize=(10, 6)
)

ax.imshow(img)

# --------------------------------
# Draw geometry
# --------------------------------

def draw_polygon(poly):

    coords = np.array(
        poly.exterior.coords
    )

    xs = []
    ys = []

    for lon, lat in coords:

        px, py = lonlat_to_pixel(
            imagery,
            lon,
            lat
        )

        # convert global pixel
        # into patch-local pixel

        patch_x = px - patch.bounds[0]
        patch_y = py - patch.bounds[1]

        xs.append(patch_x)
        ys.append(patch_y)

    ax.plot(
        xs,
        ys,
        linewidth=2
    )

if geom.geom_type == "Polygon":

    draw_polygon(geom)

elif geom.geom_type == "MultiPolygon":

    for poly in geom.geoms:

        draw_polygon(poly)

ax.set_title(
    f"Plot {PLOT_ID}"
)

ax.axis("off")

plt.savefig(
    "plot1145_overlay.png",
    bbox_inches="tight"
)

print(
    "Saved plot1145_overlay.png"
)
