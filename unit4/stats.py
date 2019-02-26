import random as r
import numpy as n
import scipy.stats as st
import sys
import time
import math
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from scipy.stats.mstats import mquantiles

n_tests = 100
version = 1

workspace = 'C:/data/'
fileName = 'SRTM_Jocko2.tif'
uri = workspace + fileName
fileInfo = QFileInfo(uri)
lyr = QgsRasterLayer(uri, fileInfo.baseName())
if not lyr.isValid():
   print "\nLayer failed to load!"
else:
    print "\nLayer " + lyr.name() + " successfully set up"

times = []
q = range(1,11,1)
p = []
Q = len(q)
for i in range(Q):
    p.append(q[i]/float(Q))
benchmarks = mquantiles(range(1,n_tests+1),p)
for i in range(Q):
    benchmarks[i] = int(math.floor(benchmarks[i]))
print ''

if True:
   pass
   
sys.stdout.write('Testing candidate script, code version ' + str(version) +  ' (' + str(n_tests) + ' tests): ')
for test in range(n_tests):
   if (test+1) in benchmarks:
      sys.stdout.write(str(int(p[0]*100)) + '%..')
      n.delete(benchmarks,0)
      p.pop(0)
   start = time.time()
   
   ncols = lyr.width() 
   nrows = lyr.height() 
   mbr_pts = lyr.extent().toString().split(':')
   mbr_coords = []
   for i in range(2): 
      vertex = mbr_pts[i].split(',')
      for j in range(2):
         mbr_coords.append(float(vertex[j]))
   x_range = abs(mbr_coords[0] - mbr_coords[2])
   y_range = abs(mbr_coords[1] - mbr_coords[3])
   x_res = x_range/ncols
   y_res = y_range/nrows
   origin = [mbr_coords[0],mbr_coords[3]]
   data = lyr.dataProvider()
  
   i = 0
   if version == 1:
      z = n.zeros(ncols*nrows)
      for col in range(ncols):
         for row in range(nrows):
            x = origin[0] + col*x_res
            y = origin[1] - row*y_res
            cursor = QgsPoint(x, y)
            ident = data.identify(cursor, QgsRaster.IdentifyFormatValue)
            if ident.isValid():
               if  ident.results()[1] == None:
                  z[i] = -99999
               else:
                   z[i] = ident.results()[1]   
            else:
               z[i] = -99999
            i = i + 1
      nulls_tags = z == -99999
      nonulls_n = sum(-nulls_tags)
      summation = n.sum(z[-nulls_tags])
      z_mean = summation/nonulls_n
      
   else:
      summation = 0
      for col in range(ncols):
         for row in range(nrows):
            x = origin[0] + col*x_res
            y = origin[1] - row*y_res
            cursor = QgsPoint(x, y)
            ident = data.identify(cursor, QgsRaster.IdentifyFormatValue)
            if ident.isValid():
               if  ident.results()[1] != None:
                  summation = summation + ident.results()[1]   
                  i = i + 1
      z_mean = summation/i
         
   end = time.time()
   secs_lapsed = end-start
   times.append(secs_lapsed)
      
def describeReport (data):
   describe = st.describe(data)
   print 'Summary statistics'
   print ''
   print '   Observations: ', str(describe [0])
   print '   Min: ', str(describe [1][0])
   print '   Max: ', str(describe [1][1])
   print '   Average: ', str(describe [2])
   print '   Median:', str(n.median(data))
   print '   Sigma: ', str(describe [3]**0.5)
   print '   Skewness: ', str(describe [4])
   print '   Kurtosis: ', str(describe [5])
   print ''
   return None

print '\n'
print '1) Code runtime'
print ''
describeReport(times)

if version == 1:
   print '2) Raster layer'
   print ''
   describeReport(z[-nulls_tags])
