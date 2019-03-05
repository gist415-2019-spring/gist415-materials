Working with Terrain Data
Terrain or elevation data is useful for many GIS Analysis and it is often used in maps. QGIS has good terrain processing capabilities built-in. In this tutorial, we will work through the steps to generate various products from elevation data such as contours, hillshade etc.

Overview of the task
The task is to create contours and hillshade map for area around Mt. Everest.

Other skills you will learn
Searching and downloading freely available terrain data.
Exporting a vector layer as KML and viewing it in Google Earth.
Get the data
We will be working with GMTED2010 dataset from USGS. This data can be downloaded from the USGS Earthexplorer site. GMTED (Global Multi-resolution Terrain Elevation Data) is a global terrain dataset that is the newer version of GTOPO30 dataset.

Here is how to search and download the revelant data from USGS Earthexplorer.

Go to the USGS Earthexplorer . In the Search Criteria tab, search for the place name Mt. Everest. Click on the result to select the location.
../_images/1156.png
In the Data Sets tab, expand the Digital Elevation group, and check GMTED2010.
../_images/2109.png
You can now skip to the Results tab and see the part of the dataset intersecting your search criteria. Click the Download Options button. You will have to log in to the site at this point. You can create a free account if you do not have one.
../_images/366.png
Select the 30 ARC SEC option and click Select Download Option.
../_images/443.png
You will now have a file named GMTED2010N10E060_300.zip. Elevation data is distributed in various raster formats such as ASC, BIL, GeoTiff etc. QGIS supports a wide variety of raster formats via the GDAL library. The GMTED data comes as GeoTiff files which are contained in this zip archive.

For convenience, you can download a copy of the data directly from below.

GMTED2010N10E060_300.zip

Data Source: [GMTED2010]

Procedure
Open Layer ‣ Add Raster Layer and browse to the downloaded zip file.
../_images/544.png
There are many different files generated from different algorithms. For this tutorial, we will use the file named 10n060e_20101117_gmted_mea300.tif.
../_images/641.png
You will see the terrain data rendered in the QGIS Canvas. Each pixel in the terrain raster represents the average elevation in meters at that location. The dark pixels represent areas with low altitude and lighter pixels represent areas with high altitude.
../_images/741.png
Let’s find our area of interest. From Wikipedia, we find that the coordinates for our area of interest - Mt. Everest - is located at the coordinates 27.9881° N, 86.9253° E. Note that QGIS uses the coordinates in (X,Y) format , so you must use the coordinates as (Longitude, Latitude). Paste 86.9253,27.9881 these at the bottom of QGIS window where it says Coordinate and press Enter. The viewport will be centered at this coordinate. To zoom in, Enter 1:1000000 in the Scale field and press Enter. You will see the viewport zoom to the area around the Himalayas.
../_images/838.png
We will now crop the raster to this area of interest. Select the Clipper tool from Raster ‣ Extraction ‣ Clipper.
Note

The Raster menu in QGIS comes from a core plugin called GdalTools. If you do not see the Raster menu, enable the GdalTools plugin from Plugins ‣ Manage and install plugins ‣ Installed. See Using Plugins for more details.

../_images/938.png
In the Clipper window, name your output file as everest_gmted30.tif. Select the Clipping mode as Extent.
../_images/1037.png
Keep the Clipper window open and switch to the main QGIS window. Hold your left mouse button and draw a rectangle covering the full canvas.
../_images/1157.png
Now back in the Clipper window, you will see the coordinates auto-populated from your selection. Make sure the Load into canvas when finished option is checked, and click OK.
../_images/1237.png
Once the process finishes, you will see a new layer loaded in QGIS. This layer covers only the area around Mt. Everest.Now we are ready to generate contours. Select the contour tool from Raster ‣ Extraction ‣ Contour.
../_images/1335.png
In the Contour dialog, select everest_gmted30 as the Input file. Name the Output file for contour lines as everest_countours.shp. We will generate contour lines for 100m intervals, so put 100 as the Interval between contour lines. Also check the Attribute name option so elevation value will be recorded as attribute of each contour line. Click OK.
../_images/1434.png
Once the processing is complete, you will see contour lines loaded into the canvas. Each line in this layer represents a particular elevation. All points along a countour line in the underlying raster would be at the same elevation. The closer the lines, the steeper the slope. Let’s inspect the contours a bit more. Right click on the contours layer and choose Open Attribute Table.
../_images/1532.png
You will see that each line feature has an attribute named ELEV. This is the height in metres that each line represents. Click on the column header a couple of times to sort the values in descending order. Here you will find the line representing the highest elevation in our data, i.e. Mt. Everest.
../_images/1630.png
Select the top row, and click on the Zoom to selection button.
../_images/1728.png
Switch to the main QGIS window. You will see the selected contour line highlighted in yellow. This is the area of the highest elevation in our dataset.
../_images/1828.png
Now let us create a hillshade map from the raster. Select Raster ‣ Analysis ‣ DEM (Terrain Models).
../_images/1926.png
In the DEM (Terrain Models) dialog, choose everest_gmted30 as the Input file. Name the Output file as everest_hillshade.tif. Choose Hillshade as the Mode. Leave all other options as is. Make sure the Load into canvas when finished option is checked, and click OK.
../_images/2022.png
Once the process finishes, you will see yet another raster loaded into QGIS canvas. Since you maybe zoomed-in near the Mt.Everest region, right click on the everest_hillshade layer and choose Zoom to Layer Extent.
../_images/2125.png
Now you will see the full extent of the hillshade raster.
