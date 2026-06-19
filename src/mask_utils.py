import numpy as np
import cv2

def polygon_to_mask(shape, polygon_pixels):
    """
    shape = (height, width)
    polygon_pixels = Nx2 array of pixel coordinates
    """

    mask = np.zeros(shape, dtype=np.uint8)

    pts = np.array(
        polygon_pixels,
        dtype=np.int32
    )

    cv2.fillPoly(
        mask,
        [pts],
        255
    )

    return mask