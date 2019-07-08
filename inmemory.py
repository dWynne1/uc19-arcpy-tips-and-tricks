"""
Geoprocessing tools support two memory workspace: 'in_memory' and 'memory'.
The 'memory' workspace was added at Pro 2.3

They are often significantly faster than writing to on-disk formats. Data
written into memory is temporary and is deleted when the application is
closed, so it is an ideal location to write intermediate data
"""

import arcpy
import os
from my_time_utils import timing

arcpy.env.overwriteOutput = True


@timing
def buffer_test(input_fc, out_workspace):

    for i in range(3):
        input_fc = arcpy.Buffer_analysis(
            input_fc, '{}\\fc_{}'.format(out_workspace, i), '100 meters')


if __name__ == "__main__":
    fc = os.path.join(os.path.dirname(__file__),
                      "world_airports.gdb\\Airports")
    layer_name = 'airport_layer'

    # Select a subset of the input feature class
    arcpy.MakeFeatureLayer_management(fc, layer_name)
    arcpy.SelectLayerByAttribute_management(layer_name,
                                            where_clause='OBJECTID < 100')

    buffer_test(layer_name, arcpy.env.scratchGDB)
    buffer_test(layer_name, 'in_memory')
    buffer_test(layer_name, 'memory')
