# inspect_score.py

from bhume import score
import inspect

print(inspect.signature(score))
print()
print(inspect.getsource(score))