Calculating Line Lengths and Statistics
QGIS has built-in functions to calculate various properties based on the geometry of the feature - such as length, area, perimeter etc. This tutorial will show how to use Field Calculator to add a column with a value representing length of each feature.

Overview of the task
We will use a polyline shapefile of railroads in North America and try to determine the total length of railroads in the United States.

Other skills you will learn
Using expressions to select features.
Re-projecting a layer from Geographic to Projected Coordinate Reference System(CRS).
Viewing statistics for values of an attribute in a layer.
Get the data
Natural Earth has a public domain railroads dataset. Download the North America supplement zip file from the portal.

For convenience, you may directly download a copy of the dataset from the link below:

ne_10m_railroads_north_america..zip

Data Source [NATURALEARTH]

Procedure
Go to Layer ‣ Add Vector Layer.
../_images/150.png
Browse to the ne_10m_railroads_north_america.zip file and click OK.
../_images/227.png
In the Select layers to add... dialog, choose ne_10m_railroads_north_america.shp layer.
../_images/324.png
Once the layer is loaded, you will notice that the layer has lines representing railroads for all of North America. Since we want to calculate line lengths only for United States railroads, we need to select the lines that fall in the United States. Right-click on the layer and select Open Attribute Table.
../_images/411.png
The layer has an attribute called sov_a3. This is the 3 letter code for the country that a particular feature falls in. We can use the value of this attribute to select features that are in USA.
../_images/511.png
In the Attribute Table window, click the Select features using an expression button.
../_images/610.png
A new dialog Select By Expression will open. Find the attribute sov_a3 under Fields and Values in the Functions list section. Double-click on it to add it to the Expression text area. Complete the expression by typing in "sov_a3" = 'USA'. Click Select followed by Close.
../_images/711.png
Back in the main QGIS window, you will see that all lines that fall in USA are selected and appear in yellow.
../_images/89.png
Now let’s save our selection to a new shapefile. Right-click on the ne_10m_railroads_north_america layer and select Save Selection As....
../_images/911.png
Click Browse and name the output file as usa_railroads.shp. We also want to change the CRS of the layer. Click on Browse next to CRS.
Note

The built-in functions that use a feature’s geometry for calculation use the units of the layer’s CRS. Geographic Coordinate Reference System(CRS) such as EPSG:4326 have degrees as units - so the length of the feature would be in degrees and area in square degrees - which is meaningless. You need to use a Projected Coordinate Reference System with units of meters or feet to perform such calculations.

../_images/109.png
Since we are interested in calculating length, let’s select an equidistance projection. Type north america equ in the Filter search box. In the results pane below, select North_America_Equidistant_Conic EPSG:102010 as the CRS. Click OK.
../_images/1114.png
In the Save vector layer as... dialog, check the Add saved file to map and click OK.
../_images/1212.png
Once the export process finishes, you will see a new layer usa_railroads loaded in QGIS. You can uncheck the box next to ne_10m_railroads_north_america layer to turn it off as we don’t need it anymore.
../_images/1311.png
Right-click on the usa_railroads layer and select Open Attribute Table.
../_images/1410.png
Now it is time to add a column with length of each feature. Put the layer in editing mode by clicking on the Toggle editing button. Once in editing mode, click the Open field calculator button.
../_images/1510.png
In the Field Calculator, check Create a new field. Enter length_km as the Output field name. Choose Decimal number (real) as the Output field type. Change the output Precision to 2. In the Function list panel, find the $length under Geometry. Double-click it to add it to the Expression. Complete the expression as $length / 1000 because our layer CRS is in meters unit and we want the output in km. Click OK.
../_images/169.png
Back in Attribute Table, you will see a new column length_km appear. Click the Toggle editing button to save the changes to the attribute table.
../_images/178.png
Now that we have length of each individual line in our layer, we can easily add it all up and find the Total length. Go to Vector ‣ Analysis Tools ‣ Basic Statistics.
../_images/189.png
Select the Input Vector layer as usa_railroads. Choose the Target field as length_km and click OK. You will see various statistics appear. The Sum value is the total length of the railroads that we are looking to find.
Note

This answer will vary slightly if a different projection is chosen.In practice, line lengths for roads and other linear features are measured on the ground and provided as attributes to the dataset. This method works in absence of such attribute and as an approximation of actual line lengths.

