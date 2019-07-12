"""
In a cursor, row values are accessed by index.
Good for performance, not as good for code readability

Alternatively, can convert to a dictionary on the fly, and access by name
"""

import arcpy
import os


def cursor_access_as_dict(table, field_names):
    """
    arcpy.da cursor values are returned in a tuple and accessed by index

    While efficient, should be sure to document what the index values return
    """

    with arcpy.da.SearchCursor(table, field_names) as cursor:
        for row in cursor:
            print('{} is at an elevation of {}'.format(row[5], row[8]))

            # exit early for demo purposes
            break


def cursor_access_as_tuple(table, field_names):
    """
    Alternatively, if you convert to a dictionary, it'll often be more clear
    what values you're accessing.

    Note: converting to a dictionary has a performance trade off though
    """

    with arcpy.da.SearchCursor(table, field_names) as cursor:
        for row in cursor:
            d = dict(zip(cursor.fields, row))
            print('{} is at an elevation of {}'.format(d['name'], d['elevation_']))

            # exit early for demo purposes
            break


if __name__ == "__main__":

    fc = os.path.join(os.path.dirname(__file__),
                      "world_airports.gdb\\Airports")
    fields = '*'

    cursor_access_as_tuple(fc, fields)
    cursor_access_as_dict(fc, fields)
