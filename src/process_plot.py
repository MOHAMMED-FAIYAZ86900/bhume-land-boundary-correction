from bhume import patch_for_plot
from bhume.geo import open_imagery

from src.edges import extract_edges

def process_plot(
    imagery,
    row
):

    geom = row["geometry"]

    patch = patch_for_plot(
        imagery,
        geom
    )

    edges = extract_edges(
        patch.image
    )

    return {
        "plot_number": str(
            row["plot_number"]
        ),
        "status": "flagged",
        "confidence": 0.0,
        "geometry": geom,
        "edge_pixels": int(
            (edges > 0).sum()
        )
    }