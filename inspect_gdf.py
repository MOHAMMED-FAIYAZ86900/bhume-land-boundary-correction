# inspect_gdf.py

from bhume import load

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

print(type(village.plots))
print()

print(village.plots.columns)
print()

print(village.plots.head())