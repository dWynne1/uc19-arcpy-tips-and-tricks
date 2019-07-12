# Gather the map project and data frame containing a feature class
aprx = arcpy.mp.ArcGISProject(r'C:\Users\andr7495\Desktop\ESRI\UC 2018\Intro to GP Python Tools\Intro_GP_Script_Tools_2018\Intro_GP_Script_Tools_2018.aprx')
m = aprx.listMaps('Map')[0]

# Create the SD-draft file
arcpy.mp.CreateWebLayerSDDraft(m, r'C:\Users\andr7495\Desktop\catdata.sddraft', 'catdata')

# Create staging file (contains all the necessary information to share a web layer, web tool, or service)
sd_output_filename = r'C:\Users\andr7495\Desktop\catdata.sd'
arcpy.StageService_server(r'C:\Users\andr7495\Desktop\catdata.sddraft', r'C:\Users\andr7495\Desktop\catdata.sd')

# Upload to AGOL or Portal
arcpy.UploadServiceDefinition_server(sd_output_filename, "My Hosted Services")

# Demos included in doc. for all the aforementioned functions