import cv2
import numpy as np

def extract_edges(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )

    gray = cv2.GaussianBlur(
        gray,
        (5,5),
        0
    )

    edges = cv2.Canny(
        gray,
        50,
        150
    )

    return edges