Making a Map¶
Often one needs to create a map that can be printed or published. QGIS has a powerful tool called Print Composer that allows you to take your GIS layers and package them to create maps.

Overview of the task
The tutorial shows how to create a map of Japan with standard map elements like map inset, grids, north arrow, scale bar and labels.

Other skills you will learn
Using ‘on-the-fly’ CRS transformation to visualize your data in a different projection.
Get the data
We will use the Natural Earth dataset - specifically the Natural Earth Quick Start Kit that comes with beautifully styled global layers that can be loaded directly to QGIS.

Download the Natural Earth Quickstart Kit.

Data Source [NATURALEARTH]

Procedure
Download and extract the Natural Earth Quick Start Kit data. Open QGIS. Click on File ‣ Open Project.
../_images/1106.png
Browse to the directory when you had extracted the natural earth data. You should see a file named Natural_Earth_quick_start_for_QGIS.qgs. This is the project file that contains styled layers in QGIS Document format. Click Open.
../_images/258.png
You would see a lot of layers in the table of content and a styled world map in the QGIS canvas. If you see errors displayed at the top of the canvas, click on the cross to close it.
../_images/339.png
In this tutorial, we will make a map of Japan. Click the Zoom In button and draw a rectangle around Japan to zoom to the area.
../_images/424.png
You can turn off some map layers for data that we do not need for this map. Un-check the box next to 10m_geography_marine_polys and 10m_admin_0_map_units layers. Before we make a map suitable for printing, we need to choose an appropriate projection. This dataset comes in Geographic Coordinate System (GCS) where the units are degrees. This is not appropriate for a map where you want the distances to be in kilometers or miles. We need to use a Projected Coordinate System that minimizes distortions for our region of interest and has units in meters. Universal Transverse Mercator (UTM) is a decent choice for a projected coordinate system. It is also global, so it’s a good default that you can rely on and choose a UTM zone that contains your area of interest to minimize distortions for your region. In our case, we will use UTM Zone 54N. Click the CRS Status button at the bottom-right of the QGIS window.
Note

For Japan, Japan Plane Rectangular CS is a projected coordinate reference system (CRS) that is designed for minimum distortions. It is divided in 18 zones and if you are working for a smaller region in Japan, using this CRS will be better.

../_images/524.png
Check the Enable on-the-fly CRS Transformation box. Type Tokyo utm zone54n in the Filter search box. Once you see the results, select Tokyo / UTM Zone 54N - EPSG:3095. Click Apply.
../_images/622.png
Now we can start to assemble our map. Go to Project ‣ New Print Composer.
../_images/722.png
You will be prompted to enter a title for the composer. You can leave it empty and click Ok.
Note

Leaving the composer name empty will assign a default name such as Composer 1.

../_images/820.png
In the Print Composer window, click on Zoom full to display the full extent of the Layout. Now we would have to bring the map view that we see in the QGIS Canvas to the composer. Go to Layout ‣ Add Map.
../_images/1019.png
Once the Add Map button is active, hold the left mouse button and drag a rectangle where you want to insert the map.
../_images/1123.png
You will see that the rectangle window will be rendered with the map from the main QGIS canvas. The rendered map may not be covering the full extent of our interest area. Select Layout ‣ Move item content to pan the map in the window and center it in the composer.
../_images/1221.png
Let us adjust the zoom level for the given map. Click on the Item Properties tab and enter 7000000 for Scale value.
../_images/1320.png
Now we will add a map inset that shows a zoomed in view for the Tokyo area. Before we make any changes to the layers in the main QGIS window, check the Lock layers for map item and Lock layer styles for map item boxes. This will ensure that if we turn off some layers or change their styles, this view will not change.
../_images/1418.png
Switch to the main QGIS window. Use the Zoom In button to zoom to the area around Tokyo.
../_images/1518.png
There are some duplicate labels coming from the ne_10m_populated_places layer. You can turn it off for this view.
../_images/1616.png
We are now ready to add the map inset. Switch the the Print Composer window. Go to Layout ‣ Add Map.
../_images/1715.png
Drag a rectangle at the place where you want to add the map inset. You will now notice that we have 2 map objects in the Print Composer. When making changes, make sure you have the correct map selected. Select the Map 1 object that we just added from the Items panel. Select the Item properties tab. Scroll down to the Frame panel and check the box next to it. You can change the color and thickness of the frame border so it is easy to distinguish against the map background.
../_images/1815.png
One neat feature of the Print Composer is that it can automatically highlight the area from the main map which is represented in our inset. Select the Map 0 object from the Items panel. In the Item properties tab, scroll down to the Overviews section. Click the Add a new overview button.
../_images/1913.png
Select Map 1 as the Map Frame. What this is telling the Print Composer is that it must highlight our current object Map 0 with the extent of the map shown in the Map 1 object.
../_images/209.png
Now that we have the map inset ready, we will add a grid and zebra border to the main map. Select the Map 0 object from the Items panel. In the Item properties tab, scroll down to the Grids section. Click the Add a new grid button.
../_images/2114.png
By default, the grid lines use the same units and projections as the currently selected map projections. However, it is more common and useful to display grid lines in degrees. We can select a different CRS for the grid. Click on the change... button next to CRS.
../_images/2213.png
In the Coordinate Reference System Selector dialog, enter 4326 in the Filter box. From the results, select the WGS84 EPSG:4326 as the CRS. Click OK.
../_images/2311.png
Select the Interval values as 5 degrees in both X and Y direction. You can adjust the Offset to change where the grid lines appear.
../_images/2411.png
Scroll down to the Grid frame section and select a frame style that suits your taste. Also check the Draw coordinates box.
../_images/259.png
Adjust the Distance to map frame till the coordinates are legible. Change the Coordinate precision to 1 so the coordinates are displayed only upto the first decimal.
../_images/267.png
Now we will add a North Arrow to the map. The Print Composer comes with a nice collection of map-related images - including many types of North Arrows. Click Layout ‣ Add Image.
../_images/277.png
Holding your left mouse button, draw a rectangle on the top-right corner of the map canvas. On the right-hand panel, click on the Item Properties tab and expand the Search directories section and select the North Arrow image of your liking.
../_images/285.png
Now we will add a scale bar. Click on Layout ‣ Add Scalebar.
../_images/296.png
Click on the layout where you want the scalebar to appear. In the Item Properties tab, make sure you have chosen the correct map element for which to display the scalebar. Choose the Style that fit your requirement. In the Segments panel, you can adjust the number of segments and their size.
../_images/305.png
It is time to label our map. Click on Layout ‣ Add Label.
../_images/3112.png
Click on the map and draw a box where the label should be. In the Item Properties tab, expand the Label section and enter the text as shown below. We can enter the text as HTML as well. Check the box Render as Html so the composer will interpret the HTML tags.
<div align=center>
<h1>Map of Japan</h1>
</div>
../_images/3211.png
Similarly add another label to add the data and software credits.
../_images/3310.png
Once you are satisfied with the map, you can export it as Image, PDF or SVG. For this tutorial, let’s export it as an image. Click Composer ‣ Export as Image.
../_images/343.png
Save the image in the format of your liking. Below is the exported PNG image.
