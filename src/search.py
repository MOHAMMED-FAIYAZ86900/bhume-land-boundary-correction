from alignment import alignment_score
from mask_utils import polygon_to_mask

def find_best_shift(
    edge_image,
    polygon_pixels,
    shape
):

    best_score = -1
    second_best_score = -1

    best_dx = 0
    best_dy = 0

    for dx in range(-10,11):
        for dy in range(-10,11):

            shifted = polygon_pixels.copy()

            shifted[:,0] += dx
            shifted[:,1] += dy

            mask = polygon_to_mask(
                shape,
                shifted
            )

            score = alignment_score(
                edge_image,
                mask
            )

            if score > best_score:

                second_best_score = best_score

                best_score = score

                best_dx = dx
                best_dy = dy

            elif score > second_best_score:

                second_best_score = score

    return (
        best_dx,
        best_dy,
        best_score,
        second_best_score
    )