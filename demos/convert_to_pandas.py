"""
There is no direct arcpy function that currently convert ArcGIS data into a
pandas dataframe, but you can utilize the below technique to get your data
into a dataframe.
"""

import arcpy
import pandas
import os


def convert_to_pandas_df(table):
    """Convert a table to a pandas dataframe"""

    # Get a list of field names to display
    # - If geometry, switch to SHAPE@ token to access geometry object
    field_names = [i.name if i.type != 'Geometry' else 'SHAPE@'
                   for i in arcpy.ListFields(table) if i.type != 'OID']

    # Open a cursor to extract info and create a pandas dataframe
    with arcpy.da.SearchCursor(table, field_names) as cursor:

        df = pandas.DataFrame(data=[row for row in cursor],
                              columns=field_names)

    return df


if __name__ == "__main__":
    fc = os.path.join(os.getcwd(),
                      "world_airports.gdb\\Airports")

    data_frame = convert_to_pandas_df(fc)
    print(data_frame.head())
