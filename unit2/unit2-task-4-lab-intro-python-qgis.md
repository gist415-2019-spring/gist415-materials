# Introductionto Python programming for QGIS
Starting from 0.9 release, QGIS has optional scripting support using Python language. PyQGIS bindings depend on SIP and PyQt4given that the whole QGIS code depends on Qt libraries. There are several waysto use Python bindings in QGIS desktop, primarily:
- By automatically running Python code when QGIS starts.
- By issuing commands in the Python console within the QGISGUI.
- By creating and usingQGIS plugins in Python.
- By creating custom applications with the QGIS API. 

Python bindings are also available for QGIS Server as well:
- Starting from the 2.8 release, Python plugins are also available on QGIS Server.
- Starting from the 2.11 version, QGIS Server library has Python bindings that can be used to embed QGIS Server 
into a Python application.

There is a complete [QGIS API](http://qgis.org/api/) reference that documents the classes and methods in QGIS libraries. 
The Pythonic QGIS API is nearly identical to the API in C++. **We will not work on the API directly in this course, 
but it will be the ultimate reference for those of you willing to create QGIS plugins beyond this course.**

**1. Automatically run Python code when QGIS starts** 

There are two distinct methods to run Python code every time QGIS gets started:
 1. [PYQGIS_STARTUP environment variable](https://docs.qgis.org/2.14/en/docs/pyqgis_developer_cookbook/intro.html#id3). You can run Python code just before QGIS initialization completes by 
 setting the `PYQGIS_STARTUP` environment variable to the path of an existing Python file.
 This method is very useful for cleaning sys.path, which may have undesirable paths, or for loading the 
 initial environ without requiring a virtual environment, e.g. homebrew or MacPorts installs on Mac.
 2. The [`startup.py` file](https://docs.qgis.org/2.14/en/docs/pyqgis_developer_cookbook/intro.html#id4). 
 Every time QGIS starts, the user’s Python home directory (usually: `.qgis2/python`) is searched for a 
 file named `startup.py`. If the file exists, it is executed by the Python interpreter.
 
**2. Issue commands in Python console within QGIS**

For scripting, the integrated Python console can be opened from menu: **`Plugins`‣`PythonConsole`**:

![Python console](https://docs.qgis.org/2.14/en/_images/console.png "Python console")

The screenshot above illustrates how to get the layer currently selected in the layer list, show its ID and optionally, 
if it is a vector layer, show the feature count. For interaction with QGIS environment, there is an *`iface`* variable, 
which is an instance of *`QgsInterface`*. This interface allows access to the map canvas, menus, toolbars and other parts 
of the QGIS application. The following statements are automatically executed when the console is started:
```
from qgis.core import *
import qgis.utils
```
**3. Create and use plugins in Python**

QGIS allows enhancement of its functionality using plugins written in Python. 
The plugin installer allows users to easily fetch, upgrade and remove Python plugins. A good resource when dealing 
with plugins is to download some plugins from [plugin repository](http://plugins.qgis.org/) and examine their code. Also, the `python/plugins/` folder 
in your QGIS installation contains some plugin that you can use to learn how to develop such plugin and some of the 
most common tasks.

**4. Create custom applications based on QGIS API**

PyQGIS custom applications or standalone scripts must be 
configured to locate the QGIS resources such as projection information, providers for reading vector and 
raster layers, etc. QGIS Resources are initialized by adding a few lines to the beginning of your application or 
script. The code to initialize QGIS for custom applications and standalone scripts is similar, but examples of each 
are provided below.
**Do not use `qgis.py` as a name for your test script** — Python will not be able to import the bindings as 
the script’s name will shadow them.

**[Using PyQGIS in standalone scripts](https://docs.qgis.org/2.14/en/docs/pyqgis_developer_cookbook/intro.html#id8)**

Often when processing some GIS data, it is handy to create some scripts for automating the process instead of doing 
the same task again and again. With PyQGIS, this is possible —import the **qgis.core** module, initialize it and 
you are ready for the processing. To start a standalone script, initialize the QGIS resources at the start of the script:
```
from qgis.core import *
# supply path to qgis install location
QgsApplication.setPrefixPath("/path/to/qgis/installation", True)

# create a reference to the QgsApplication, setting the
# second argument to False disables the GUI
qgs =QgsApplication([], False)

# load providers
qgs.initQgis()

# Write your code here to load some layers, use processing algorithms, etc.
# When your script is complete, call exitQgis() to remove the provider and
# layer registries from memory
qgs.exitQgis()
```

- Line 1: Import the *qgis.core* module.
- Line 4: Configure the prefix path. The prefix path is the location where QGIS is installed on your system. 
It is configured in the script by calling the `setPrefixPath` method. The second argument ofsetPrefixPathis set to `True`, 
which controls whether the default paths are used. The QGIS install path varies by platform; the easiest way to find it 
for your system is to use the Python Console from within QGIS and get the path by running `QgsApplication.prefixPath()`.
- Line 8: Save a reference to QgsApplicationin the variable `qgs`. The second argument is set to `False`, 
which indicates that we do not plan to use the GUI since we are writing a standalone script. 
- Line 11: Load the QGIS data providers and layer registry by calling the `qgs.initQgis()` method. With QGIS initialized, 
we are ready to write the rest of the script.
- Line 17: Finally, wrap up by calling `qgs.exitQgis()` to remove the data providers and layer registry from memory.

**[Using PyQGIS in custom applications](https://docs.qgis.org/2.14/en/docs/pyqgis_developer_cookbook/intro.html#id9)**

Alternatively, you may want to create an interactive application that uses some GIS functionality —- measure some data, 
export a map in PDF or any other functionality. The `qgis.gui` module additionally brings various GUI 
components, most notably the map canvas widget that can be very easily incorporated into the application with support 
for zooming, panning and/or any further custom map tools.The only difference between using PyQGIS in standalone scripts 
and a custom PyQGIS application is the second argument when instantiating the `QgsApplication`. Pass `True` instead of `False`
to indicate that we plan to use a GUI:
```
from qgis.core import*
# supply path to qgis install location

QgsApplication.setPrefixPath("/path/to/qgis/installation", True)

# create a reference to the QgsApplication
# setting the second argument to True enables the GUI, since this is a custom application
qgs=QgsApplication([], True)

# load providersqgs.initQgis()
# Write your code here to load some layers, use processing algorithms, etc.
# When your script is complete, call exitQgis() to remove the provider and
# layer registries from memory
qgs.exitQgis()
```

**[Running Custom Applications](https://docs.qgis.org/2.14/en/docs/pyqgis_developer_cookbook/intro.html#id10)**

**You will need to tell your system where to search for QGIS libraries and appropriate Python modules if they are not 
in a well-knownlocation** —- otherwise Python will complain:

```
>>> import qgis.core
ImportError: No module named qgis.core
```
This can be fixed in two steps:
1. Set the `PYTHONPATH` environment variable on the command line. In the following commands,`qgispath` should be 
replaced with your actual QGIS installation path:

| | |
| -- | -- |
| Linux | Open command line.<br>Enter: `export PYTHONPATH=/qgispath/share/qgis/python` |
| Windows | Open command prompt.<br>Enter: `set PYTHONPATH=c:\qgispath\python2`. | 

The path to the PyQGIS modules is now known, however they depend on `qgis_core` and `qgis_gui` libraries 
(the Python modules serve only as wrappers). Path to these libraries is typically unknown for the operating system. 
Fix this by adding the directories where the QGIS libraries reside to search path of the dynamic linker:

| | |
| -- | -- |
| Linux | Open command line.<br>Enter: `export LD_LIBRARY_PATH=/qgispath/lib` |
| Windows | Open command prompt.<br>Enter: `set PATH=C:\qgispath;%PATH%` |
