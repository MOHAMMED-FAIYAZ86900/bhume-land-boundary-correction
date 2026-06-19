from bhume import load

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

print("Total plots:", len(village.plots))

for i, plot in enumerate(village.plots[:5]):

    print("\nPlot", i)

    print(type(plot))

    try:
        print(plot.geom_type)
    except:
        print("No geom_type")