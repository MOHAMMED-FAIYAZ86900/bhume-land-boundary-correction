from confidence import compute_confidence

print(
    compute_confidence(
        120,
        40
    )
)

print(
    compute_confidence(
        120,
        118
    )
)

def determine_status(
    confidence
):

    if confidence >= 0.60:
        return "corrected"

    return "flagged"
