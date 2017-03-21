# -*- coding: utf-8 -*-

import glob
import os


#from qgis_functions import qgis_api
#from grass_api import grass_api
from qd_grass_functions import qd_grass
#from automatisation_classification_otb import otb_classification
#from automatisation_segmentation_otb import otb_segmentation


def pause():

    raw_input("Press Enter to continue...")


def main():

    # Workspace parameter
    workspace = r"E:\Etude\APP\Qualite_drainage"
    dem = r"E:\Etude\APP\Qualite_drainage\ProjetAPP\DEM.tif"        ## devra être le dem généré par le lidar dans le futur


    ####### QGIS and GRASS Parameters
    grassPath = r"E:\OSGeo4W\bin\grass72.bat"      #setting ordinateur local APP
    dbPath = workspace + "\\" + "ProjetAPP"
    location = "newLocation"
    mapset = "PERMANENT"
    mapName = "mapName"

    # ---------- GRASS ----------#

    grass = qd_grass(grassPath,dbPath,location,mapset)

    dem_name = "DEM"
    #grass.loc_from_file(dem)

    grass.import_file(dem,dem_name)

    dem_filled1 = "DEM_filled1"
    direction = "direction"
    grass.fill_dir(dem_name,dem_filled1,direction)

    dem_filled2 = "DEM_filled2"
    grass.fill_nulls(dem_filled1,dem_filled2)

    threshold = 1000
    stream_raster = "Stream_raster"
    stream_vector = "Stream_vector"
    grass.stream_extract(dem_filled2,threshold,stream_raster,stream_vector)


if __name__ == "__main__":
    main()



