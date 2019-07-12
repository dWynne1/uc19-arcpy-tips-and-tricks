"""
If you are ever searching for specific parameter information, combine the
ListTools and GetParameterInfo functions.

I use this frequently when hunting for different geoprocessing tools may have
been set up.
"""

import arcpy

search = '*_management'

for tool in arcpy.ListTools(wild_card=search):
    for p in arcpy.GetParameterInfo(tool):
        if p.parameterType == 'Derived' and p.datatype == 'Long':
            print('Tool: {}\n    parameter: {}'.format(tool, p.displayName))
