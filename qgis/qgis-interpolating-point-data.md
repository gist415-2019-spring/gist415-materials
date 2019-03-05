Interpolating Point Data¶
Interpolation is a commonly used GIS technique to create continuous surface from discrete points. A lot of real world phenomena are continuous - elevations, soils, temperatures etc. If we wanted to model these surfaces for analysis, it is impossible to take measurements throughout the surface. Hence, the field measurements are taken at various points along the surface and the intermediate values are inferred by a process called ‘interpolation’. In QGIS, interpolation is achieved using the built-in Interpolation plugin.

Overview of the task
We will take field depth measurements for a Lake Arlington in Texas and create an elevation relief map and contours from these measurements.

Other skills you will learn
Creating contours from point data.
Masking no-data values from a raster layer.
Adding labels to a vector layer.
Get the data
Texas Water Development Board provides the shapefiles for completed lake surveys.

Download the 2007-12 survey shapefiles for Lake Arlington.

For convenience, you can directly download the sample data used in this tutorial from link below.

Shapefiles.zip

Data Sources: [TWDB]

Procedure
Open QGIS. Go to Layer ‣ Add Layer ‣ Add Vector Layer..
../_images/1104.png
Browse to the downloaded Shapefiles.zip file and select it. Click Open.
../_images/250.png
In the Select layers to add... dialog, hold the Shift key and select Arlington_Soundings_2007_stpl83.shp and Boundary2004_550_stpl83.shp layers. Click OK.
../_images/337.png
You will see the 2 layers loaded in QGIS. The Boundary2004_550_stpl83 layer represents the boundary of the lake. Un-check the box next to it in the Table of Contents.
../_images/422.png
This will reveal the data from the second layer Arlington_Soundings_2007_stpl83. Though the data looks like lines, it is a series of points that are very close.
../_images/522.png
Click the Zoom icon and select a small area on the screen. As you zoom closer, you will see the points. Each point represents a reading taken by a Depth Sounder at the location recorded by a DGPS equipment.
../_images/620.png
Select the Identify tool and click on a point. You will see the Identify Results panel show up on the left with the attribute value of the point. In this case, the ELEVATION attribute contains the depth of the lake at the location. As our task is to create a depth profile and elevation contours, we will use this values as input for the interpolation.
../_images/720.png
Make sure you have the Interpolation plugin enabled. See Using Plugins for how to enable plugins. Once enabled, go to Raster ‣ Interpolation ‣ Interpolation.
../_images/818.png
In the Interpolation dialog, select Arlington_Soundings_2007_stpl83 as the Vector layers in the Input panel. Select ELEVATION as the Interpolation attribute. Click Add. Change the Cellsize X and Cellsize Y values to 5. This value is the size of each pixel in the output grid. Since our source data is in a projected CRS with Feet-US as units, based on our selection, the grid size will be 5 feet. Click on the ... button next to Output file and name the output file as elevation_tin.tif. CLick OK.
Note

Interpolation results can vary significantly based on the method and parameters you choose. QGIS interpolation supports Triagulated Irregular Network (TIN) and Inverse Distance Weighting (IDW) methods for interpolation. TIN method is commonly used for elevation data whereas IDW method is used for interpolating other types of data such as mineral concentrations, populations etc. See the Spatial Analysis module of the QGIS documentation for more details.

../_images/919.png
You will see the new later elevation_tin loaded in QGIS. Right-click the layer and select Zoom to layer.
../_images/1017.png
Now you will see the full extent of the created surface. Interpolation does not give accurate results outside the collection area. Let’s clip the resulting surface with the lake boundary. Go to Raster ‣ Extraction ‣ Clipper.
../_images/1121.png
Name the Output file as elevation_tin_clipped.tif. Select the Cliiped mode as Mask layer. Select Boundary2004_550_stpl83 as the Mask layer`. Click OK.
../_images/1219.png
A new raster elevation_tin_clipped will be loaded in QGIS. We will now style this layer to show the difference in elevations. Note the min and max elevation values from the elevation_tin layer. Right-click the elevation_tin_clipped layer and select Properties.
../_images/1318.png
Go to the Style tab. Select Render type as Singleband pseudocolor. In the Generate new color map panel, select Spectral color ramp. As we want to create a depth-map as opposed to a height-map, check the Invert box. This will assign blues to deep areas and reds to shallow areas. Click Classify.
../_images/1416.png
Switch to the Tranparency tab. We want to remove the black-pixels from our output. Enter 0 as the Additional no data value. Click OK.
../_images/1516.png
Now you have a elevation relief map for the lake generated from the individual depth readings. Let’s generate contours now. Go to Raster ‣ Extraction ‣ Contours.
../_images/1614.png
In the Contour dialog, enter contours as the Output file for contour lines. We will generate contour lines at 5ft intervals, so enter 5.00 as the Interval between contour lines. Check the Attribute name box. Click OK.
../_images/1713.png
The contour lines will be loaded as contours layer once the processing is finished. Right-click the layer and select Properties.
../_images/1813.png
Go to the Labels tab. Check the Label this layer with box and select ELEV as the field. Select Curved as the Placement type and click OK.
../_images/1911.png
You will see that each contour line will be appropriately labeled with the elevation along the line.
../_images/207.png
