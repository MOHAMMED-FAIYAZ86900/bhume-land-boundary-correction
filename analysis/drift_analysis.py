import geopandas as gpd
import numpy as np

official = gpd.read_file(
    "data/34855_vadnerbhairav_chandavad_nashik/input.geojson"
)

truth = gpd.read_file(
    "data/34855_vadnerbhairav_chandavad_nashik/example_truths.geojson"
)

truth_ids = set(truth["plot_number"])

matches = official[
    official["plot_number"].isin(truth_ids)
]

dxs = []
dys = []

for _, row in matches.iterrows():

    plot_id = row["plot_number"]

    truth_geom = truth[
        truth["plot_number"] == plot_id
    ].geometry.iloc[0]

    official_geom = row.geometry

    dx = (
        truth_geom.centroid.x -
        official_geom.centroid.x
    )

    dy = (
        truth_geom.centroid.y -
        official_geom.centroid.y
    )

    dxs.append(dx)
    dys.append(dy)

print("Mean dx:", np.mean(dxs))
print("Mean dy:", np.mean(dys))

print("Median dx:", np.median(dxs))
print("Median dy:", np.median(dys))