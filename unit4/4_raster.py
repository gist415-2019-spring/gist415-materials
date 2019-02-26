'''
File name:   4_raster.py
Date:        4-10-2018
Author:      UA, MS-GIST, GIST 415

Abstract:    Demonstrates basic raster data handling with QGIS

Instructions: 1. Read the code.
              2. Answer the questionnaire that follows the code (SRTM_Jocko.tiff is included in the lab).
              3. Submit your work in three files:
                   * A raster_name.py file with the source code modified by you (i.e. Questions 2 to 6).
                   * A metadata report file generated with meta_to_file.
                   * A text document narrative_name.docx with your narrative of the code (i.e. Question 1).  

In the file names, substitute 'name' by your family name.
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def meta_to_file (layer, folder, fname):
    print '\nExporting metadata of ' + layer.name() + ' to file at:' 
    print '\tFolder:\t' + folder[0:-1] 
    print '\tFile:\t\t' + fname + '.txt'
    f = open(folder + fname + '.txt','w') 
    f.write(layer.metadata()) 
    f.close() 

workspace = 'C:/Users/fsanc/data/'
fileName = 'SRTM_Jocko.tiff'
fileInfo = QFileInfo(workspace + fileName)
lyr = QgsRasterLayer(workspace + fileName, fileInfo.baseName())
if not lyr.isValid():
   print "\nLayer failed to load!"
else:
    print "\nLayer " + lyr.name() + " successfully set up"
   
print ""
print '##########'
print ' Layer summary '
print '##########'
print ""
print 'Number of columns:\t' + str(lyr.width()) 
print 'Number of rows:\t' + str(lyr.height())
pts = lyr.extent().toString().split(':')
coords_mbr = []
for i in range(2): 
   vertex = pts[i].split(',')
   for j in range(2):
      coords_mbr.append(float(vertex[j])) 
print 'Layer bounds:' 
print '\tWest:\t\t' + str(round(coords_mbr[0],2))
print '\tEast:\t\t\t' + str(round(coords_mbr[2],2))
print '\tSouth:\t\t' + str(round(coords_mbr[1],2))
print '\tNorth:\t\t' + str(round(coords_mbr[3],2))
print 'Number of bands:\t' + str(lyr.bandCount())

lyr_type = lyr.rasterType()
if lyr_type == 0:
    print ('Layer is:\t\t\tGrayOrUndefined, single band')
elif lyr_type == 1:
    print ('Layer is:\t\t\tPalette, single band')
else:
    print ('Layer is:\t\t\tMultiband')
print 'Renderer type is:\t'  + lyr.renderer().type()

meta_to_file(lyr,workspace,'report_' + lyr.name())

print ""
print '############'
print ' Rendering settings '
print '############'
print ""
print 'Resetting rendering variables...\n'
lst = [QgsColorRampShader.ColorRampItem(0, QColor(255,255,0)), \
          QgsColorRampShader.ColorRampItem(3000, QColor(255,0,0))]
fcn = QgsColorRampShader()
fcn.setColorRampType(QgsColorRampShader.INTERPOLATED)
fcn.setColorRampItemList(lst)
shader = QgsRasterShader()
shader.setRasterShaderFunction(fcn)
renderer = QgsSingleBandPseudoColorRenderer(lyr.dataProvider(), 1, shader)
lyr.setRenderer(renderer)
print 'Renderer type is:\t'  + lyr.renderer().type()

print ''
print '#########'
print ' Spatial query '
print '#########'
print ''

data = lyr.dataProvider()
cursor = QgsPoint(266269, 329801)
print 'Cursor at\t\tX\t\tY'
print "\t\t\t" + str(int(cursor.x())) + '\t' + str(int(cursor.y()))
print ''
sys.stdout.write('Value(s):')
ident = data.identify(cursor, QgsRaster.IdentifyFormatValue)
if ident.isValid():
   value = ident.results()
   for band in range(1,lyr.bandCount()+1):
      if band == 1:
         indentation = '\t\t'
      else:
          indentation = '\t\t\t\t'
      print indentation + 'Band ' + str(band) + ': ' + str(value[band])

print '\nDone'


'''
Questions:

1) Explain in plain English, and line by line, the meaning of the above source code.

2) Change the code in the element meta_to_file so that the output file extension is not txt but xml. Create a metadata report file.

3) Change the workspace folder and layer name in the code so it can successfully read the input data in your machine.

4) Out of the metadata report file, get the layer's Data Type and Spatial Reference System values. The SRS should be in Proj4 format.

5) By using the 'Spatial Query' section in the source code, pick three separate locations in the layer and retrieve their elevation values.

6) Set the Color Ramp Type of the QgsColorRampShader() function object to have an DISCRETE QgsColorRampShader value.

'''
