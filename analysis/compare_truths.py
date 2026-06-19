import geopandas as gpd
import matplotlib.pyplot as plt

official = gpd.read_file(
    "data/34855_vadnerbhairav_chandavad_nashik/input.geojson"
)

truth = gpd.read_file(
    "data/34855_vadnerbhairav_chandavad_nashik/example_truths.geojson"
)

truth_ids = truth["plot_number"]

official_small = official[
    official["plot_number"].isin(truth_ids)
]

ax = official_small.plot(
    edgecolor="blue",
    facecolor="none",
    figsize=(10,10)
)

truth.plot(
    ax=ax,
    edgecolor="red",
    facecolor="none"
)

plt.title("Blue=Official Red=Truth")
plt.show()