# debug_overlay.py

from bhume import load
from bhume.geo import (
    open_imagery,
    geom_to_imagery_crs
)

VILLAGE_DIR = (
    "data/34855_vadnerbhairav_chandavad_nashik"
)

village = load(VILLAGE_DIR)

imagery = open_imagery(
    f"{VILLAGE_DIR}/imagery.tif"
)

geom = village.plot("1145")

geom_3857 = geom_to_imagery_crs(
    imagery,
    geom
)

print("Original:")
print(geom.bounds)

print("\nImagery CRS:")
print(geom_3857.bounds)