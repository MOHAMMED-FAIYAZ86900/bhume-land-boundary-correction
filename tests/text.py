from bhume import load, patch_for_plot
from bhume.geo import open_imagery

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

src = open_imagery(
    "data/34855_vadnerbhairav_chandavad_nashik/imagery.tif"
)

plot = village.plot("1145")

patch = patch_for_plot(
    src,
    plot
)

print(type(patch.image))

try:
    print("Shape:", patch.image.shape)
except:
    print("No shape attribute")

print("\nImage object:")
print(patch.image)