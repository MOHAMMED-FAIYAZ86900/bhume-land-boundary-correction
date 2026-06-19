from bhume import load
from src.predictor import run

village = load(
    "data/34855_vadnerbhairav_chandavad_nashik"
)

predictions = run(village)

print("Predictions:", len(predictions))

print("\nFirst Prediction:")
print(predictions[0])