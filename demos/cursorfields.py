"""
arcpy.da cursor support using "*" to access all fields.

As a general rule, it's better to use only the fields you need (especially
for performance).
"""


import arcpy
import os
from my_time_utils import timing


@timing
def cursor_fields(table, fields):
    """
    Minimal wrapping of arcpy.da.SearchCursor to demonstrate performance
    with different number of fields
    """

    with arcpy.da.SearchCursor(table, fields) as cursor:
        for row in cursor:
            values = row


if __name__ == "__main__":

    # Test dataset has 200,000+ points with 97 fields
    fc = os.path.join(os.path.dirname(__file__),
                      "data.gdb\\Popular_BG_points")

    cursor_fields(fc, '*')  # ignore first run

    # Access just two fields
    cursor_fields(fc, ['NAME', 'STATE_NAME'])

    # Access all fields (97)
    cursor_fields(fc, '*')
