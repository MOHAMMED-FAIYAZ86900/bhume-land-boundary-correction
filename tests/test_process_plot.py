from bhume import load
from bhume.geo import open_imagery

from src.process_plot import process_plot

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

imagery = open_imagery(
    "data/34855_vadnerbhairav_chandavad_nashik/imagery.tif"
)

row = village.plots.iloc[0]

result = process_plot(
    imagery,
    row
)

print(result)