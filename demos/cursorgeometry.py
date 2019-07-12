"""
When accessing geometry information, it's better to access for only what you
need.

If you need the full geometry, go ahead, but if you need only specific geometry
information, use geometry tokens instead (SHAPE@XY, SHAPE@AREA, etc.)
"""

import arcpy
import os
from my_time_utils import timing


@timing
def cursor_geometry_xy(table):
    """Access centroid information via the geometry object's centroid"""
    with arcpy.da.SearchCursor(table, 'SHAPE@') as cursor:
        for row in cursor:
            centroid = row[0].trueCentroid
            xy = centroid.X, centroid.Y


@timing
def cursor_just_xy(table):
    """Access centroid information via the SHAPE@XY token"""
    with arcpy.da.SearchCursor(table, 'SHAPE@XY') as cursor:
        for row in cursor:
            xy = row[0]


if __name__ == "__main__":
    fc = os.path.join(os.path.dirname(__file__),
                      "world_airports.gdb\\Airports")

    # ignore first due to initialization time costs
    cursor_geometry_xy(fc)

    # Access just two
    cursor_geometry_xy(fc)

    # Access all fields
    cursor_just_xy(fc)
