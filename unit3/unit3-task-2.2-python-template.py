'''
Unit    3
Task    2.2
Worth   2 points
Effort  3.5 hrs (est.)
Topic   QGIS programming: projections support
'''

#################
# Learning aims #
#################
'''
This script demonstrates how to run the following tasks:

    1) Create a CSR object with long-lat WGS 1984 attributes, using an EPSG/PostGIS CRS ID.
    2) Create a CSR object with UTM 16 (WGS 1984 datum) attributes, using the Proj4 standard.
    3) Report CSR properties to standard output.
    4) Reproject coordinates from one CSR to another.

EPSG, WKT, Proj4 and other formats for many CSR setups are available at:

* SpatialReference.org  http://spatialreference.org
* EPSG Registry:        http://www.epsg-registry.orgs

This lab makes use of these online resources to access CSR ID's and details of such definitions.
'''

##################### 
# Training exercise #
#####################
'''
The task of this lab is to reproject the location of Capital One Arena from lat-long WGS 1984 to UTM 18.

Capital One Arena is home to several sports teams in the District of Columbia:

   - NBA's Washington Wizards.
   - NHL's Washington Capitals,
   - WNBA's Washington Mystics,
   - AFL's Washington Valor,
   - NCAA's Georgetown Hoyas men's basketball team.

The venue's post address is: 601 F Street NW, Washington, DC, 20004
'''

####################################
# Source code template begins here #
####################################

unitTags = ['Meters','Feet','Degrees','UnknownUnit','DecimalDegrees','DegreesMinutesSeconds', 'DegreesDecimalMinutes'] 

print '\nStarting script 2.2 of Unit 3...\n'

#
# 1. Creation of a CSR object with long-lat WGS 1984 attributes, using an EPSG/PostGIS CRS ID
#
'''
* The search engines of SpatialReference.org and the EPSG Registry may look somewhat cumbersome at first.
* If you are familiar with CRS codes, though, both catalogs come in handy.
* To know the EPSG code of long-lat WGS 1984, you can enter the following values in the Registy Search Engine:

    - Name: WGS 84
    - Area: World

* It will return a list of coordinate systems based on WGS 1984.
* The one at the world level is at the top of the list, with EPSG code = 4326.
'''

crs_src = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.PostgisCrsId)
if crs_src.isValid():
   print 'CRS source object successfully built:'
   print  crs_src.toProj4(), '\n'

#
# 2. Creation of CSR object with UTM 16 (WGS 1984 datum) attributes, using the Proj4 standard
#
'''
* UTM details are more easily retrieved with the SpatialReference.org search engine.
* DC is in UTM 18 North.
* By searching "WGS 84 / UTM zone 18N" you are given the UTM Zone 18N details for the WGS 84 spheroid model.
* The human readable OGC WKT is:

  PROJCS["WGS 84 / UTM zone 18N",
    GEOGCS["WGS 84",
        DATUM["WGS_1984",
            SPHEROID["WGS 84",6378137,298.257223563,
                AUTHORITY["EPSG","7030"]],
            AUTHORITY["EPSG","6326"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.01745329251994328,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4326"]],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["latitude_of_origin",0],
    PARAMETER["central_meridian",-75],
    PARAMETER["scale_factor",0.9996],
    PARAMETER["false_easting",500000],
    PARAMETER["false_northing",0],
    AUTHORITY["EPSG","32618"],
    AXIS["Easting",EAST],
    AXIS["Northing",NORTH]]

* The Proj4 expression, on the other hand, is more concise:

    +proj=utm +zone=18 +ellps=WGS84 +datum=WGS84 +units=m +no_defs
'''

proj = "+proj=utm +zone=18 +ellps=WGS84 +datum=WGS84 +units=m +no_defs"
crs_dtn = QgsCoordinateReferenceSystem()
crs_dtn.createFromProj4(proj)
if crs_dtn.isValid():
   print 'CRS destination object successfully built:'
   print crs_dtn.toProj4(), '\n'

#
# 3. Reporting of CRS properties
#
'''
Although not mandatory, it is good practice to have the columns be straight. The tab symbol ('\t') can help.
'''

print '\t\t\t\t\tSource CSR\t\tDestination CSR'
print "QGIS CRS ID:", '\t\t\t',crs_src.srsid(),'\t\t\t',crs_dtn.srsid()
print "PostGIS SRID:", '\t\t\t', crs_src.postgisSrid(),'\t\t\t',crs_dtn.postgisSrid()
print "Description:",'\t\t\t', crs_src.description(),'\t\t',crs_dtn.description()
print "Projection Acronym:", '\t\t',crs_src.projectionAcronym(),'\t\t\t',crs_dtn.projectionAcronym()
print "Ellipsoid Acronym:", '\t\t',crs_src.ellipsoidAcronym(),'\t\t\t',crs_dtn.ellipsoidAcronym()
print "Is geographic:", '\t\t\t',crs_src.geographicFlag(),'\t\t\t\t',crs_dtn.geographicFlag()
print "Map units:", '\t\t\t', unitTags[crs_src.mapUnits()],'\t\t\t',unitTags[crs_dtn.mapUnits()]
print ''

#
# 4. Reprojection of coordinates
#
'''
According to Google Maps, Capital One Arena's long-lat WGS 1984 coordinates are long = -77.021, lat = 38.897.
'''
site_src = QgsPoint(-77.021,38.897)
reproj = QgsCoordinateTransform(crs_src, crs_dtn)
site_dtn = reproj.transform(site_src)
print "X coordinate at site:",'\t\t',round(site_src.x(),3),'\t\t\t', int(site_dtn.x())
print "Y coordinate at site:",'\t\t',round(site_src.y(),3),'\t\t\t', int(site_dtn.y())

##################################
# Source code template ends here #
##################################


#############
# YOUR TURN #
#############
'''
You are required to do the following tasks:

    a. Adapt the above source code to locate the Hollywood Sign -- the iconic letters atop Mount Lee in Los Angeles, CA.
         - The Sign is located about 2,000 ft norteast of Lake Hollywood Park (3160 Canyon Lake Dr, Los Angeles, CA 90068).
         - Specifically, you are asked to: reproject the long-lat WGS 1984 coordinates of the Sign to "WGS 84 / UTM zone 11N".
         - Feel free to use Google Maps or Google Earth to find out the long-lat WGS 1984 coordinates of the Hollywood Sign.
    b. Use the right number of '\t' to make sure that columns in the report remain straight.
    c. The name of your site's variables should not start with the word 'site' (as in the template code) but with 'sign'.
    d. Ask the following question: What do the built-in functions round() and int() do?    

    * Submit to D2L your source code. You do not need to include the above template, just the adapted version with your modifications.
    * The case study is just an excuse to assess your programming skills 
    * To assess the lab, the instructor will run your code in his/her machine, so please make sure it does not crash.
'''
