from bhume import load, patch_for_plot
from bhume.geo import (
    open_imagery,
    geom_to_imagery_crs,
    lonlat_to_pixel,
)

import matplotlib.pyplot as plt
import numpy as np

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

src = open_imagery(
    "data/34855_vadnerbhairav_chandavad_nashik/imagery.tif"
)

plot = village.plot("1145")

patch = patch_for_plot(src, plot)

print("Patch bounds:", patch.bounds)
print("Patch shape:", patch.image.shape)

print(type(plot))
print(plot.geom_type)