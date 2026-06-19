from bhume import load
from src.geometry_utils import shift_geometry

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

row = village.plots.iloc[0]

geom = row["geometry"]

shifted = shift_geometry(
    geom,
    0.00005,
    0.00005
)

print(
    geom.centroid
)

print(
    shifted.centroid
)