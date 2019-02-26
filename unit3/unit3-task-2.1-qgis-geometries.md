# Unit 3. Open Source production and software licensing
## Activity No. 
2.1
## Type of Activity 
Lab
## Worth 
2 points
## Time effort 
3.5 hrs (est.)
## Topic 
QGIS programming: geometry handling
### Introduction
Points, linestrings and polygons representing spatial features are commonly referred to as geometries. In
QGIS they are expressed by the `QgsGeometry` class. Sometimes a feature is actually a collection of simple
or “single-part” geometries. Such a feature is called a “multi-part” geometry. If it contains just one type
of simple geometry, we call it multi-point, multi-linestring or multi-polygon. For example, the state of
Alaska consists of mainland and many islands and as a whole it can be represented as a multi-polygon.

### Building [geometries](https://docs.qgis.org/2.14/en/docs/pyqgis_developer_cookbook/geometry.html#id1)
There are several options for creating a geometry with the `QgsGeometry` class:
_Passing pairs of coordinates_

#### Building a point feature
```gPoint = QgsGeometry.fromPoint(QgsPoint(1,2))```
- Note that coordinates are to be passed to the point constructor inside a `QgsPoint` class object.
#### Building a polyline feature
```gLine = QgsGeometry.fromPolyline([QgsPoint(1,2), QgsPoint(3,4)])```
- Coordinates are to be passed to the polyline constructor as a list of `QgsPoint` class objects.
- The polyline (linestring) geometry consists of an ordered list of points.
#### Building a polygon feature
```gPolygon = QgsGeometry.fromPolygon([[QgsPoint(1,2), QgsPoint(3,4), QgsPoint(5,6)]])```
- Coordinates are to be passed to the polygon constructor as a list of linear rings, i.e. closed
linestrings. Note that a linestring is, in turn, a list of `QgsPoint` class objects.
- The first linear ring is an outer ring (i.e., the boundary of the polygon.)
- Optional subsequent rings are holes in the polygon.

Multi-part geometries go one level further, so a multi-point is a list of points, a multi-linestring is a list of
linestrings, and a multi-polygon is a list of polygons. For instance,
#### Building a multipoint feature
```
gPoint1 = QgsGeometry.fromPoint(QgsPoint(1,1))
gPoint2 = QgsGeometry.fromPoint(QgsPoint(2,2))
gPoint3 = QgsGeometry.fromPoint(QgsPoint(3,3))
gMPoint = QgsGeometry.fromMultiPoint([gPoint1, gPoint2, gPoint3])
```

_Passing a Well-Known Text (WKT) string_
#### Building a point feature
```
feature = QgsGeometry.fromWkt("POINT(3 4)")
```
- WKT is a text markup language for representing vector geometries. Originally developed by the
Open Geospatial Consortium and described in the “Simple Feature Access” and “Coordinate
Transformation Service” specifications, the current definition is described in the ISO/IEC 13249-
3:2016 standard, "Information technology – Database languages – SQL multimedia and application
packages – Part 3: Spatial" (SQL/MM) and in ISO 19162:2015, "Geographic information – Wellknown text representation of coordinate reference systems".

_Passing a Well-Known Binary (WKB) object_
#### Setting a geometry with WKB
```
feature = QgsGeometry()
feature.setWkbAndOwnership(wkb, len(wkb))
```
- Line 1: an empty geometry is created.
- Line 2: the geometry is set up with details passed in WKB format. WKB is equivalent to WTK and is
used to transfer and store the same information on database systems.

### [Accessing](https://docs.qgis.org/2.14/en/docs/pyqgis_developer_cookbook/geometry.html#id2) geometries
To know the geometry type of a feature, you must follow two steps:
1. Call the feature’s `wkbType()` or `geometrytype()` methods.
2. Compare the return value with QGIS geometry definitions in the `QGis.WkbType` enumeration (if
`wkbType()` is used) or in the `QGis.GeometryType` enumeration (if `geometrytype()` is used). See
[https://qgis.org/api/2.0/classQGis.html](https://qgis.org/api/2.0/classQGis.html) for a comprehensive definition of QGIS enumerations.

#### Checking the object’s geometry type with QGis.WkbType
```
gPoint.wkbType() == QGis.WKBPoint
# Returns True
gLine.wkbType() == QGis.WKBLineString
# Returns True
gPolygon.wkbType() == QGis.WKBPolygon
# Returns True
gPolygon.wkbType() == QGis.WKBMultiPolygon
# Returns False
```
- This script presumes you have already created `gPoint`, `gLine`, and `gPolygon` with the scripts
demonstrated in the prior section of this tutorial.
- Lines 1, 4, 7, 10: The two steps described above are combined in a single command.

There is also a logic method `isMultipart()` to find out whether a geometry is multipart or not:

#### Checking the object’s geometry type
```
print gPoint.isMultipart()
# Prints 1 (i.e. True)
```
- This script presumes you have already created `gPoint` with the scripts demonstrated in the prior
section of this tutorial.

To extract the geometric data of a geometry there are getter methods for every vector class:
#### Getting coordinate data from geometries
```
gPoint.asPoint()
#Returns (1,2)
gLine.asPolyline()
#Returns [(1,2), (3,4)]
gPolygon.asPolygon()
#Returns [[(1,2), (3,4), (5,6), (1,2)]]
```
- This script presumes you have already created `gPoint`, `gLine`, and `gPolygon` with the scripts
demonstrated in the prior section of this tutorial.
- Note how the presence and number of square brackets (which represent, respectively, a single pair
of coordinates, a list of pairs, and a list of lists) help differentiate points, lines and polygons.
- The closing point in polygons is explicit, meaning that the first and last points in the list of point
coordinates are the same.
- Multipart geometries have similar getter methods: `asMultiPoint()`, `asMultiPolyline()`,
`asMultiPolygon()`.
- The format `(value1, value2)` represents `(x,y)` coordinates but it is not a Python tuple. Actually, it is
a `QgsPoint` object and has `x()` and `y()` methods to access single coordinate values:
```
# Using the above point object:
gPoint.asPoint().x()
#Returns 1
gPoint.asPoint().y()
#Returns 2
```
To extract objects in a vector dataset, the dataset’s getFeatures() method can be combined with a Python
iterator:

#### Getting layer features
```
features = layer.getFeatures()
for f in features:
 print f. wkbType()
 ```
- This script presumes you have already created a layer object that points to a vector dataset. See
Unit 2’s lab for an introduction about loading layers.

### Using [geometry predicates and operations](https://docs.qgis.org/2.14/en/docs/pyqgis_developer_cookbook/geometry.html#id3)
QGIS uses the GEOS library for advanced geometry operations such as:
- Topology predicates: contains(), intersects().
- Boolean set arithmetic: union(), difference().
- Geometric measurements (line length, polygon perimeter, polygon area).

In the below example, features in a dataset called layer are iteratively read and used for a few geometric
calculations:
#### Getting features’ measurements
```
features = layer.getFeatures()
for f in features:
 geom = f.geometry()
 print "Area: ", geom.area()
 print "Perimeter: ", geom.length()
```
- Again, this script presumes you have already created a layer object that points to a vector dataset.

*CAUTION*

The above `QgsGeometry` class’ `area()` and `length()` methods do not take Coordinate Reference System
settings into account, so geodetic relationships are not computed. For more powerful area and distance
calculations, the `QgsDistanceArea` class can be used:

#### Turning geodetic operations on
```
geoCalculator = QgsDistanceArea()
geoCalculator.setEllipsoidalMode(True)
print "distance in meters: ", geoCalculator.measureLine(QgsPoint(10,10),QgsPoint(11,11))
geoCalculator.setEllipsoidalMode(False)
print "distance in meters: ", geoCalculator.measureLine(QgsPoint(10,10),QgsPoint(11,11))
```
- Line 3: Projection capabilities are turned on so calculations are done on the ellipsoid. If an ellipsoid
is not set explicitly, WGS84 parameters are used for calculations.
- Line 6: Projections are turned off so calculations are planar.

### Script examples
You can find many examples of algorithms that are included in QGIS and use these methods to analyze
and transform vector data:
- Handling of QGIS geometries: [Multi-part to single-part algorithm](https://raw.github.com/qgis/QGIS/release-2_0/python/plugins/processing/algs/ftools/MultipartToSingleparts.py)
- Computation of distances and areas: [Distance matrix algorithm](https://raw.github.com/qgis/QGIS/release-2_0/python/plugins/processing/algs/ftools/PointDistance.py)
