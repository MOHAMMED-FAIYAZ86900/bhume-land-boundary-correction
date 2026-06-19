from bhume import load

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

plot = village.plots[0]

print(type(plot))
print()

print(dir(plot))