# inspect_pixel.py

from bhume.geo import lonlat_to_pixel
import inspect

print(inspect.signature(lonlat_to_pixel))
print()
print(inspect.getsource(lonlat_to_pixel))