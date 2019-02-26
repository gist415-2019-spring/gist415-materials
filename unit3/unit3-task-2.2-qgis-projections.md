# Unit 3. Open Source production and software licensing
## Activity No. 
2.2
## Type of Activity 
Lab
## Worth 
2 points
## Time effort 
3.5 hrs (est.)
## Topic 
QGIS programming: projections support

### [Coordinate reference systems](https://docs.qgis.org/2.14/en/docs/pyqgis_developer_cookbook/crs.html#id1)
Feature coordinates refer to one of the many Coordinate Reference Systems (CRS) that are recognized by
QGIS. CRS details are encapsulated inside of `QgsCoordinateReferenceSystem` class objects. Instances of
this class can be created by different object constructors, which are called based on the parameters
passed to the constructor:

_Specify CRS by its CRS ID_

#### Creating a QgsCoordinateReferenceSystem class object
```
crs = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.PostgisCrsId)
if crs.isValid():
 print ‘CRS object correctly created’
```
- Line 1: this constructor uses a numeric value and a label that informs of the ID system that is used.
QGIS observes three different numeric ID standards for a reference system:
    - `PostgisCrsId` — CRS ID’s used in PostGIS databases.
    - `InternalCrsId` — CRS ID’s internally used in QGIS databases.
    - `EpsgCrsId` — CRS ID’s assigned by the EPSG organization.
In the example, the CRS ID that is passed is PostGIS’ SRID 4326, which refers to WGS84.
- If the second parameter is not specified, the PostGIS ID standard is used by default.

_Specify CRS by its Well-Known Text (WKT)_
#### Creating a `QgsCoordinateReferenceSystem` class object
```
wkt = 'GEOGCS["WGS84", DATUM["WGS84", SPHEROID["WGS84", 6378137.0, 298.257223563]],'
 PRIMEM["Greenwich", 0.0], UNIT["degree",0.017453292519943295],'
 AXIS["Longitude",EAST], AXIS["Latitude",NORTH]]'
crs = QgsCoordinateReferenceSystem(wkt)
if crs.isValid():
 print ‘CRS object correctly created’
```
- Lines 1, 2: CRS expressions in WTK must be passed to the object constructor as a string.

_Specify CRS by Proj4 string_
#### Creating a `QgsCoordinateReferenceSystem` class object
```
crs = QgsCoordinateReferenceSystem()
crs.createFromProj4("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")
if crs.isValid():
 print ‘CRS object correctly created’
```
- Line 1: instead of passing the parameters to the constructor, and undefined
`QgsCoordinateReferenceSystem` object is created first.
- Line 2: the CRS is defined with the `QgsCoordinateReferenceSystem`‘s method createFromProj4(),
which must be passed a Proj4 expression as a string (to learn more about Proj4 expressions go to
[http://proj4.org/operations/index.html](http://proj4.org/operations/index.html)).

_*NOTE*_

QGIS needs to look up appropriate values in its internal database `srs.db` when initializing spatial
reference systems. Thus, when you create an independent application you need to use
`QgsApplication.setPrefixPath()` to set up the paths, otherwise it will fail to find the database. If you are
running the commands from QGIS python console or developing a plugin you do not need to worry,
everything is set up already.

_Getting CSR settings_

`QgsCoordinateReferenceSystem` objects are equipped with a large set of getter methods to access CRS
properties: `srsid()`, `postgisSrid()`, `description()`, `projectionAcronym()`, `ellipsoidAcronym()`, `toProj4()`,
`geographicFlag()`, `mapUnits()`:
#### Calling getter methods of a `QgsCoordinateReferenceSystem` object
```
print "QGIS CRS ID:", crs.srsid()
print "PostGIS SRID:", crs. postgisSrid()
print "Description:", crs.description()
print "Projection Acronym:", crs.projectionAcronym()
print "Ellipsoid Acronym:", crs.ellipsoidAcronym()
print "Proj4 String:", crs. toProj4()
# Check whether it's geographic or projected coordinate system
print "Is geographic:", crs.geographicFlag()
# Check type of map units in this CRS (values defined in QGis::units enum)
print "Map units:", crs.mapUnits()
```
- Line 12: see [https://qgis.org/api/2.0/classQGis.html](https://qgis.org/api/2.0/classQGis.html) for a comprehensive definition of QGIS
enumerations.

### Projections
You can do transformations between different spatial reference systems with the
`QgsCoordinateTransform` class. The shortest way to go uses four commands:
1. Create a source CRS.
2. Create a destination CRS.
3. Construct a `QgsCoordinateTransform` instance that transforms source coordinates to destination
coordinates.
4. Apply the `transform()` function of the trained `QgsCoordinateTransform` object to do the
transformation of coordinates.

#### Reprojecting coordinates_
```
crsSrc = QgsCoordinateReferenceSystem(4326) # WGS 84
crsDest = QgsCoordinateReferenceSystem(32633) # WGS 84 / UTM zone 33N
xform = QgsCoordinateTransform(crsSrc, crsDest)
pt1 = xform.transform(QgsPoint(18,5))
print "Transformed point:", pt1
pt2 = xform.transform(pt1, QgsCoordinateTransform.ReverseTransform)
print "Transformed back:", pt2
```
- Line 4: by default, it does forward transformation (source -> destination).
- Line 7: it is capable to do inverse transformation (destination -> source) as well.

#### Examples
- You can use this open source code to reproject the geometries in a layer: [Reproject algorithm.](https://raw.github.com/qgis/QGIS/release-2_0/python/plugins/processing/algs/ftools/ReprojectLayer.py)
