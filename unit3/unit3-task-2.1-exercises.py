'''
Unit    3
Task    2.1
Worth   2 points
Effort  3.5 hrs (est.)
Topic   QGIS programming: geometry handling


1. You must fill out the below source code with correct code. You should open this file with the QGIS Python editor and test your answers with it. 
2. Submit your source code (i.e. this Python file with your answers) to D2L.

Resources to complete this lab:

- Unit 2's lab instructions: Task 2.1 - Lab - Geometry handling instructions.pdf 
- Template source code: Task 2.1 - Lab - Python template.py. Open the source code in the QGIS Python editor and run it to see its behavior.
- Also use comments below.

Please work on the above resources in the order they are listed here.

Basically, you should use Task 2.1 - Lab - Python template.py as code that needs to be modified by following Task 2.1 - Lab - Geometry handling instructions.pdf and comments below.

'''


# 1)  Build a linestring feature based on coordinates.

'''
Instead of a polygon object, build a linestring object made of three point objects with (x,y) coordinates (0,0), (1,1), (2,2)
'''

# 2) Build a lineastring feature based on WKT.

'''
The WKT expression of a linestring is LINESTRING(x y, x y, x y, etc). For instance, LINESTRING(5 2, 3 1) for a linestring going from (5,2) to (3,1)

Use a WKT expression to build a linestring object with (x,y) coordinates (0,0), (1,1), (2,2)
'''

# 3) Get the geometry type of the features.

'''
Replicate the command in Unit 3 - Lab Section 1.py
'''

# 4) Get the vertex coordinates of the linestring feature and print them in columns. For example:

'''
string = linestring1.asPolyline()
n_vertices = len(string)
for vertex in range(n_vertices):
    print '\t' + str(string[vertex])
print '
'''

# 5) Compute the bounding box of the linestring feature.

'''
Instead of computing the average x and y coordinates of a polygon geometry, let's computed the bounding box (i.e. Minimum Bounding Rectangle) of the linestring:

n_vertices = len(geom)
x = []
y = []
for vertex in range(n_vertices-1):
   x.append(geom[vertex].x())
   y.append(geom[vertex].y())
mbr = {'lowerLeft': (min(x), min(y)),'upperRight':(max(x), max(y))}
'''

# 6) Get the area and perimeter of the polygon geometry.

'''
Because linestring have no area, you just have to call the lenght() method of your linestring object.
'''

# 7) Print a report on the MBR and length measurements to standard output.

'''
Replicate the command in Unit 3 - Lab Section 1.py
'''

