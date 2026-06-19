import geopandas as gpd

gdf = gpd.read_file(
    "data/34855_vadnerbhairav_chandavad_nashik/input.geojson"
)

print(gdf.isnull().sum())
print("\nColumns:")
print(gdf.columns)

print("\nTotal plots:")
print(len(gdf))

print("\nSample:")
print(gdf.head())

print(gdf["map_area_sqm"].describe())

print(gdf["recorded_area_sqm"].describe())

valid = gdf[
    (gdf["recorded_area_sqm"].notna()) &
    (gdf["recorded_area_sqm"] > 0)
].copy()

valid["area_ratio"] = (
    valid["map_area_sqm"] /
    valid["recorded_area_sqm"]
)

print(valid["area_ratio"].describe())

