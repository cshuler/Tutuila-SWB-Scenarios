# This script simply splits the island wide land use coverage into major watershed sections for buffering

import arcpy 
import os
	
arcpy.env.overwriteOutput = True
workingdir = "C:\\Users\\cshul\\Desktop\\temp"
	
# make individual land use shapefiles
for i in (range(0,33)):
    arcpy.Select_analysis(os.path.join(workingdir, "Maj_WSheds.shp"),  os.path.join(workingdir, "tempselect.shp"), '"FID" = {}'.format(i))
    arcpy.Clip_analysis(os.path.join(workingdir, "LU_Big_simp_3.shp"), os.path.join(workingdir, "tempselect.shp"),  os.path.join(workingdir, 'outs', "LU_simp3_clipped_{}.shp".format(i)))
	
	
	
	