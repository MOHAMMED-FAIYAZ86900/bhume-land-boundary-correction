from shapely.affinity import translate

def shift_geometry(
    geometry,
    dx,
    dy
):
    return translate(
        geometry,
        xoff=dx,
        yoff=dy
    )