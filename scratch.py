"""
The scratchGDB (and scratchFolder) environment locations will always be available
to you. If you need to write out intermediate data to a reliable location, use these
environments.
"""

import arcpy

print("scratch gdb is {}".format(arcpy.env.scratchGDB))

arcpy.Delete_management(arcpy.env.scratchGDB)

# scratchGDB (and scratchFolder) will always exist if you need it
if arcpy.Exists(arcpy.env.scratchGDB):
    print("scratch gdb is {}".format(arcpy.env.scratchGDB))
