print("Startin' up!")

from arcpy import mp
from pprint import pprint

print("Writin' to file!")

with open(r"C:\auto_result.txt", 'w') as result_file:
	pprint("hello from {}!".format(mp), stream=result_file)

input("All set! Press any button to quit.")