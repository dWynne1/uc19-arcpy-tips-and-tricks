import arcpy
from pprint import pprint

desc_old = arcpy.Describe(r'C:\Users\andr7495\Desktop\ESRI\UC 2019\ArcPy Tips and Tricks\DebugDemo\DebugDemo.gdb\CatSightings')
type(desc_old)  # returns an arcpy.Describe object
dir(desc_old)  # returns an empty list

desc_new = arcpy.da.Describe(r'C:\Users\andr7495\Desktop\ESRI\UC 2019\ArcPy Tips and Tricks\DebugDemo\DebugDemo.gdb\CatSightings')
type(desc_new)  # dict
pprint(desc_new)
