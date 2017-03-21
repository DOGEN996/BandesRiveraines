import gdal
from gdalconst import *


mnt_file= r'D:\IVBR\DEM_filled.tif'
search_dist = 1000
n_iteration = 0


mnt = gdal.Open(mnt_file, GA_Update)

mnt_band = mnt.GetRasterBand(1)


gdal.FillNodata(targetBand = mnt_band, maskBand=None, maxSearchDist = search_dist, smoothingIterations = n_iteration)

mnt = None