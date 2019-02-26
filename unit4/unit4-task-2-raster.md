# Using Raster Layers

## 1. Layer Properties
A raster layer consists of one or more raster bands. A band represents a matrix of values. Color imagery
(e.g. aerial photo) is a raster dataset consisting of red, blue and green bands. Single band layers typically
represent either continuous variables (e.g. elevation) or discrete variables (e.g. land use). In some cases,
a raster layer comes with a palette and raster values refer to colors stored in the palette.

Below is an abridged list of getter methods for raster dataset objects in QGIS:

|  |  |
| -- | -- |
| `width()` | Returns the layer’s number of columns. |
| `height()` | Returns the layer’s number of rows. |
| `extent().toString()` | Returns the bounding box of the layer as a string. |
| `rasterType()` | Returns the layer’s type of color domain and band(s). |
| `bandCount()` | Returns the layer’s number pf bands. |
| `metadata()` | Returns publisher’s data about the layer. |

For example:
```
>>> rlayer.width(), rlayer.height()
(812, 301)
>>> rlayer.extent()
<qgis._core.QgsRectangle object at 0x000000000F8A2048>
>>> rlayer.extent().toString()
u'12.095833,48.552777 : 18.863888,51.056944'
>>> #0 = GrayOrUndefined (single band), 1 = Palette (single band), 2 = Multiband
>>> rlayer.rasterType()
2
>>> rlayer.bandCount()
3
>>> rlayer.metadata()
u'<p class="glossy">Driver:</p>...'
```

## 2. Renderer
When a raster layer is loaded, it gets a default renderer based on its type. to query the current renderer:
```
>>> rlayer.renderer()
<qgis._core.QgsSingleBandPseudoColorRenderer object at 0x7f471c1da8a0>
>>> rlayer.renderer().type()
u'singlebandpseudocolor'
```

to set a renderer you can call the `setRenderer()` method in the `QgsRasterLayer` object. There are several
available renderer classes that can be returned from the `QgsRasterRenderer` methods:

|  |  |
| -- | -- |
| `QgsMultiBandColorRenderer()` | For multiband layers mapping the bands to RGB colors. |
| `QgsPalettedRasterRenderer()` | For single band layers with a palette, drawn using the palette. |
| `QgsSingleBandColorDataRenderer()` | For single band layers mapping to band to a color channel. |
| `QgsSingleBandGrayRenderer()` | For single band layers in grayscale (min = black, max = white). |
| `QgsSingleBandPseudoColorRenderer()` | For single band raster layers in pseudocolor. |

### Single band rasters
Let’s say we want to render our raster layer (assuming one band only) with colors ranging from green to
yellow (for pixel values from 0 to 255). This is done in two steps:
```
>>> lst = [ QgsColorRampShader.ColorRampItem(0, QColor(0,255,0)), \
 QgsColorRampShader.ColorRampItem(255, QColor(255,255,0)) ]
>>> fcn = QgsColorRampShader()
>>> fcn.setColorRampType(QgsColorRampShader.INTERPOLATED)
>>> fcn.setColorRampItemList(lst)
>>> shader = QgsRasterShader()
>>> shader.setRasterShaderFunction(fcn)
>>> renderer = QgsSingleBandPseudoColorRenderer(layer.dataProvider(), 1, shader)
>>> layer.setRenderer(renderer)
```
- Line 1: A color ramp is created from pixel value 0 and RGB color (0,255,0) to pixel value 255 and
RGB color (255, 255, 0). The color map is provided as a list of items with pixel value and its
associated color.
- Line 2: A shader function object is created to color the layer as specified by a color map.
- Line 3: A color ramp type is set up for the shader function. Three modes of interpolation of color
values can be used:
   - Linear ( `INTERPOLATED` ): pixel colors are linearly interpolated from the color map entries
above and below the actual pixel value.
   - Discrete ( `DISCRETE` ): color is used from the color entry with equal or higher value.
   - Exact ( `EXACT` ): only pixels with value equal to color map entries are drawn.
- Line 4: The shader function loads the color ramp.
- Line 5: A raster shader object is created.
- Line 6: The raster shader object loads a shader function.
- Line 7: A single band pseudocolor renderer object is created by passing:
   - An interface to the layer data (as returned by the data provider).
   - The band number (raster bands are indexed beginning at one).
   - The shader object.
- Line 8: The raster layer loads the renderer.

### Multiband rasters
By default, QGIS maps the first three bands to red, green and blue values to create a color image. This is
the MultiBandColor drawing style. In some cases, you might want to override these settings. The
following code interchanges red band (1) and green band (2):
```
>>> rlayer.renderer().setGreenBand(1)
>>> rlayer.renderer().setRedBand(2)
```

In case only one band is necessary for visualization of the raster, single band drawing can be chosen —
either gray levels or pseudocolor.

### 3. Refreshing Layers
If you do change layer symbology and would like to ensure that the changes are immediately visible to
the user, call these methods:
```
if hasattr(layer, "setCacheImage"):
 layer.setCacheImage(None)
layer.triggerRepaint()
```
- Line 1-2: ensure the cached image of the rendered layer is erased if render caching is on.
- Line 3: force any map canvas containing the layer to issue a refresh.

If you have changed layer symbology you might want to force QGIS to update it in the layer list (legend)
widget. This can be done as follows ( `iface` is an instance of `QgisInterface`):

```
iface.legendInterface().refreshLayerSymbology(layer)
```

### 4. Query Values
to do a query on value of bands of raster layer at some specified point:
```
data = rlayer.dataProvider()
ident = data.identify(QgsPoint(15.30, 40.98), QgsRaster.IdentifyFormatValue)
if ident.isValid():
 print ident.results()
```
- Line 1: create an interface to the layer data (as returned by the data provider).
- Line 2: retrieve the pixel value at location (15.30,40.98).
- Line 3: if the value is successfully retrieved, run Line 4.
- Line 4: The `results()` method of the identify object returns a dictionary, with band indices as keys
and band values as values: `{1: 17, 2: 220}`
