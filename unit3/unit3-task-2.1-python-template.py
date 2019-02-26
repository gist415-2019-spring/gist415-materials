'''
Unit    3
Task    2.1
Worth   2 points
Effort  4 hrs (est.)
Topic   QGIS programming: handling geometries

This script demonstrates how to run the following tasks:

1) Build a polygon feature with holes, based on coordinates.		
2) Build a polygon feature with holes, based on WKT.		
3) Get the geometry type of the features.
4) Get the vertex coordinates of a feature and print them in columns.
5) Compute the mean center of the geometry.	
6) Get the area and perimeter of the geometry. ,			
7) Print out a report of the geometric measures of the geometry to standard output.
'''

WktTypeTags = ['WKBUnknown','WKBPoint','WKBLineString','WKBPolygon','WKBMultiPoint',\
                        'WKBMultiLineString','WKBMultiPolygon','WKBNoGeometry','WKBPoint25D',\
                        'WKBLineString25D','WKBPolygon25D','WKBMultiPoint25D','WKBMultiLineString25D',\
                        'WKBMultiPolygon25D'] 

print '\nStarting script 2.1 of Unit 3...\n'

# 1)  Build a polygon feature with holes, based on coordinates.

point1 = QgsPoint(0,0)
point2 = QgsPoint(0,1)
point3 = QgsPoint(1,1)
point4 = QgsPoint(1,0)
point5 = QgsPoint(0.25,0.25)
point6 = QgsPoint(0.25,0.75)
point7 = QgsPoint(0.75,0.75)
point8 = QgsPoint(0.75,0.25)

square_ring1 = QgsGeometry.fromPolygon([[point1, point2, point3, point4],[point5, point6, point7, point8]])

# 2) Build a polygon feature with holes, based on WKT.
#     The output shape is identical to that of square_ring1.

square_ring2 = QgsGeometry.fromWkt("POLYGON ((0 0, 0 1, 1 1, 1 0),(0.25 0.25, 0.25 0.75, 0.75 0.75, 0.75 0.25))")

# 3) Get the geometry type of the features.

print 'Geometry type of object 1: ' + str(WktTypeTags[square_ring1.wkbType()])
print 'Geometry type of object 2: ' + str(WktTypeTags[square_ring2.wkbType()])
print ''

# 4) Get the vertex coordinates of a feature and print them in columns.
#     From now on only square_ring1 is used.

print 'Printing coordinates of square_ring1...\n'
geom = square_ring1.asPolygon()
n_rings = len(geom)
for ring in range(n_rings):
    print '\tVertices of ring ' + str(ring + 1) + ':'
    n_vertices = len(geom[ring])
    for vertex in range(n_vertices):
        print '\t' + str((geom[ring][vertex].x(), geom[ring][vertex].y()))
    print ''

# 5) Compute the mean center of the polygon geometry.

outer = geom[0]
n_vertices = len(outer)
x = 0
y = 0
for vertex in range(n_vertices-1):
   x = x + outer[vertex].x()
   y = y + outer[vertex].y()
mean_x = x/(n_vertices-1)
mean_y = y/(n_vertices-1)

# 6) Get the area and perimeter of the polygon geometry.

perim = square_ring1.length()
area = square_ring1.area()

# 7) Print a report on the geometric measures to standard output.

print 'Printing geometric summary of square_ring1...\n'
print "\tMean Center:\t", str(mean_x) + ' ' + str(mean_y) 
print "\tArea:\t\t", area
print "\tPerimeter:\t\t", perim
