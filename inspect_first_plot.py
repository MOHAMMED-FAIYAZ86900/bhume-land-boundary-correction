# inspect_first_plot.py

from bhume import load

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

row = village.plots.iloc[0]

print(type(row))
print()

print(row)