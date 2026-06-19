# validate_predictions.py

import geopandas as gpd

gdf = gpd.read_file(
    "data/34855_vadnerbhairav_chandavad_nashik/predictions.geojson"
)

print(gdf.head())
print()
print("Rows:", len(gdf))