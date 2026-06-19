from bhume import load, write_predictions
from src.predictor import run

import geopandas as gpd

VILLAGE_DIR = (
    "data/34855_vadnerbhairav_chandavad_nashik"
)

village = load(
    VILLAGE_DIR
)

predictions_list = run(
    village
)

predictions = gpd.GeoDataFrame(
    predictions_list,
    geometry="geometry",
    crs="EPSG:4326"
)

out_path = (
    f"{VILLAGE_DIR}/predictions.geojson"
)

write_predictions(
    out_path,
    predictions
)

print(
    "Saved:",
    out_path
)

print(
    "Predictions:",
    len(predictions)
)

print(
    "\nStatus Counts:"
)

print(
    predictions["status"].value_counts()
)