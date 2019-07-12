"""
Bulk attribute creation is a common arcpy need, but there are sizable
performance differences when bulk adding many fields

Using arcpy.da.ExtendTable is a non-obvious, but efficient approach
"""

import arcpy
import numpy
from my_time_utils import timing

arcpy.env.overwriteOutput = True


@timing
def add_with_extendtable(table):
    """
    Add fields by leveraging an empty numpy array.

    Note: arcpy.da.ExtendTable has some limitations, as it doesn't have all
    options that AddField/AddFields have, but has some significant performance
    gains
    """

    # Join fields to the feature class, using ExtendTable
    in_array = numpy.array([],
                           numpy.dtype([('intfield', numpy.int32),
                                        ('Name', '|S10'),
                                        ('Descript', '|S10'),
                                        ('Type', '|S255'),
                                        ('Comment', '|S10'),
                                        ('Symbol', '|S10'),
                                        ('DateTimeS', '|S10'),
                                        ('X', numpy.float),
                                        ('Y', numpy.float),
                                        ]))

    arcpy.da.ExtendTable(table, "OID@", in_array, "intfield")


@timing
def add_field_multiple(table):
    """
    Add fields by calling AddField multiple times
    """

    arcpy.AddField_management(table, 'intfield', 'LONG')
    arcpy.AddField_management(table, 'Name', 'TEXT', field_length=10)
    arcpy.AddField_management(table, 'Descript', 'TEXT', field_length=10)
    arcpy.AddField_management(table, 'Type', 'TEXT', field_length=255)
    arcpy.AddField_management(table, 'Comment', 'TEXT', field_length=10)
    arcpy.AddField_management(table, 'Symbol', 'TEXT', field_length=10)
    arcpy.AddField_management(table, 'DateTimeS', 'TEXT', field_length=10)
    arcpy.AddField_management(table, 'X', 'FLOAT')
    arcpy.AddField_management(table, 'Y', 'FLOAT')


@timing
def add_fields(table):
    """
    Add fields using AddFields tool

    NOTE: AddFields is only in Pro. Was added with the intent of bulk adding
    fields more efficiently.
    """

    arcpy.AddFields_management(table,
                               [['infield', 'LONG'],
                                ['Name', 'TEXT', None, 10],
                                ['Descript', 'TEXT', None, 10],
                                ['Type', 'TEXT', None, 255],
                                ['Comment', 'TEXT', None, 10],
                                ['Symbol', 'TEXT', None, 10],
                                ['DateTimeS', 'TEXT', None, 10],
                                ['X', 'FLOAT'],
                                ['Y', 'FLOAT']]
                               )


if __name__ == "__main__":

    arcpy.env.workspace = arcpy.env.scratchGDB

    for i in range(1, 4):
        table_name = 'add_fields_{}'.format(i)
        arcpy.CreateTable_management(arcpy.env.scratchGDB, table_name)

    add_fields('add_fields_1')
    add_field_multiple('add_fields_2')
    add_with_extendtable('add_fields_3')
