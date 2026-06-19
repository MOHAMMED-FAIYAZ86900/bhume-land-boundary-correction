# inspect_writer.py

from bhume import write_predictions
import inspect

print(inspect.signature(write_predictions))
print()
print(inspect.getsource(write_predictions))