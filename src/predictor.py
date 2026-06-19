from src.corrector import correct_geometry


def compute_confidence(row):

    recorded_area = row["recorded_area_sqm"]
    map_area = row["map_area_sqm"]

    if (
        recorded_area is None
        or recorded_area <= 0
    ):
        return 0.30

    area_ratio = (
        map_area / recorded_area
    )

    error = abs(
        area_ratio - 1.0
    )

    confidence = (
        1.0 - error
    )

    confidence = max(
        0.10,
        min(
            0.95,
            confidence
        )
    )

    return round(
        confidence,
        3
    )


def process_plot(row):

    original_geom = row["geometry"]

    corrected_geom = correct_geometry(
        original_geom
    )

    confidence = compute_confidence(
        row
    )

    if confidence < 0.40:

        status = "flagged"

        final_geom = original_geom

    else:

        status = "corrected"

        final_geom = corrected_geom

    return {
        "plot_number": str(
            row["plot_number"]
        ),
        "status": status,
        "confidence": confidence,
        "method_note": (
            "global_shift_v2"
        ),
        "geometry": final_geom
    }


def run(village):

    predictions = []

    total = len(
        village.plots
    )

    for i, (_, row) in enumerate(
        village.plots.iterrows()
    ):

        if i % 100 == 0:

            print(
                f"Processing {i}/{total}"
            )

        prediction = process_plot(
            row
        )

        predictions.append(
            prediction
        )

    return predictions