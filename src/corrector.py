from shapely.affinity import translate

GLOBAL_DX = -0.000051
GLOBAL_DY = 0.000110


def correct_geometry(geom):

    return translate(
        geom,
        xoff=GLOBAL_DX,
        yoff=GLOBAL_DY
    )