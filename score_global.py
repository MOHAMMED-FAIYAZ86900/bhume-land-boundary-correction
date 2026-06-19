from bhume import load, score
import geopandas as gpd

VILLAGE_DIR = (
    "data/34855_vadnerbhairav_chandavad_nashik"
)

village = load(
    VILLAGE_DIR
)

preds = gpd.read_file(
    f"{VILLAGE_DIR}/predictions.geojson"
)

result = score(
    preds,
    village
)

print(result)