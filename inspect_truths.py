# inspect_truths.py

from bhume import load

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

print(type(village.example_truths))
print()

print(village.example_truths.head())
print()

print(village.example_truths.columns)