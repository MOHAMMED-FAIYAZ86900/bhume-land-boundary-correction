import numpy as np

def alignment_score(
    edge_image,
    mask
):
    """
    Score how well the mask aligns
    with image edges.
    """

    overlap = np.logical_and(
        edge_image > 0,
        mask > 0
    )

    return overlap.sum()