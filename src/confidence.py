def compute_confidence(
    best_score,
    second_best_score
):
    """
    Confidence based on how much
    better the best shift is than
    the second-best shift.
    """

    if best_score <= 0:
        return 0.0

    confidence = (
        best_score - second_best_score
    ) / best_score

    confidence = max(
        0.0,
        min(1.0, confidence)
    )

    return confidence