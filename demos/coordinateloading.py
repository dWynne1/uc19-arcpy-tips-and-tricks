"""
arcpy geometry objects can be used to create geometry when creating new
feature classes.

They are a bit object heavy in their creation, and have performance costs.

Other approaches like using JSON, or simply passing in a list of
coordinates (as below) are often easy to read and more efficient.
"""


import arcpy
import random
from my_time_utils import timing_no_args

arcpy.env.overwriteOutput = True


@timing_no_args
def create_geom_with_obj(feature_class, coords, spatial_ref=4326):
    """Create features using geometry objects"""

    with arcpy.da.InsertCursor(feature_class, 'SHAPE@') as cursor:
        for x1, y1, x2, y2 in coords:
            geometry = arcpy.Polyline(
                arcpy.Array([arcpy.Point(x1, y1), arcpy.Point(x2, y2)]),
                spatial_ref)
            cursor.insertRow([geometry])


@timing_no_args
def create_geom_with_coords(feature_class, coords):
    """Create features using just the coordinates"""

    with arcpy.da.InsertCursor(feature_class, 'SHAPE@') as cursor:
        for x1, y1, x2, y2 in coords:
            cursor.insertRow([[(x1, y1), (x2, y2)]])


def create_xy_pairs():
    """
    Small function for demo purposes to acquire a large number of coordinates.
    Normally, you'd be acquiring coordinates some other way, not just massing
    a large number of random coordinates.
    """

    random.seed(1)
    xy_list = []
    for i in range(0, 20000):
        xy_list.append((random.uniform(-156.1, -154.8),
                        random.uniform(18.9, 20.3),
                        random.uniform(-156.1, -154.8),
                        random.uniform(18.9, 20.3)))

    return xy_list


if __name__ == "__main__":

    sr = 4326
    fc = arcpy.CreateFeatureclass_management(arcpy.env.scratchGDB,
                                             'line_fc',
                                             'POLYLINE',
                                             spatial_reference=sr)[0]

    xy_pairs = create_xy_pairs()

    create_geom_with_obj(fc, xy_pairs, sr)
    create_geom_with_coords(fc, xy_pairs)
