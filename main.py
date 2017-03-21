# -*- coding: utf-8 -*-

import glob
import os
from qgis_functions import qgis_api
from grass_api import grass_api
from automatisation_classification_otb import otb_classification
from automatisation_segmentation_otb import otb_segmentation


def pause():

    raw_input("Press Enter to continue...")

def main():

    # Workspace parameter
    workspace = r"D:\IVBR"
#
#    # OTB Segmentation Parameters
#    ortho = workspace + "\\" + "OrthophotoIR" + "\\" + "cdq15007_304_f08_nir.tif"
#    ortho_name = os.path.basename(ortho)[:-4]
#
#    ranger = 7
#    spatialr = 20
#    minSize = 10
#
#    outStep1Filter = workspace + "\\" + "OTBSegmentationFiles" + "\\" + "{0}_segmentation1_filter.tif".format(ortho_name)
#    outStep2 = workspace + "\\" + "OTBSegmentationFiles" + "\\" + "{0}_segmentation2_{1}_{2}_{3}.tif".format(ortho_name,spatialr,ranger,minSize)
#    outStep3 = workspace + "\\" + "OTBSegmentationFiles" + "\\" +"{0}_segmentation3_{1}_{2}_{3}.tif".format(ortho_name,spatialr,ranger,minSize)
#    outStep4 = workspace + "\\" + "SegmentsFile" + "\\" + "SegmentsOTB_{1}_{2}_{3}.shp".format(ortho_name,spatialr,ranger,minSize)
#
#
#    # QGIS and GRASS Parameters
    grassPath = r"C:\OSGeo4W64\bin\grass70.bat"      #setting ordinateur local APP
    dbPath = workspace + "\\" + "dbGrass"
    location = "LocationProject"
    mapset = "PERMANENT"
    mapName = "mapName"
#    ruleFile = workspace + "\\" + "RuleFiles" + "\\" + "RuleFile_1.txt"
#    folderPathLASClassification = workspace + "\\" + "LASToolResults"
#
#    DEMFile = workspace + "\\" + "DEMFile" + "\\" + "DEMResample.tif"
#
#    ExportRasterGrass = dbPath + "\\" + "ExportRasterGrass" + ".tif"
#
#    TrainingSites = workspace + "\\" + "TrainingSitesFile" + "\\" + "TrainingSites" + ".shp"
#    exportArbre = workspace + "\\" + "ExportSelected" + "\\" + "ExportSelect_arbre" + ".shp"
#    exportBatiment = workspace + "\\" + "ExportSelected" + "\\" + "ExportSelect_bati" + ".shp"
#    exportArbuste = workspace + "\\" + "ExportSelected" + "\\" + "ExportSelect_arbuste" + ".shp"
#    exportSol = workspace + "\\" + "ExportSelected" + "\\" + "ExportSelect_sol" + ".shp"
#
#    #OTB Classification Parameters
#
#    #pathToOTB = "C:\\OTB-5.8.0-win64\\OTB-5.8.0-win64\\bin"
#    pathToOTB = "C:\\OTB-5.8.0-win64\\bin"
#    outComputeOGRTrainingLayerXMLFile = workspace + "\\" + "OTBClassificationFiles" + "\\" + "{0}_Classification_ComputeOGRTraningLayer.xml".format(ortho_name)
#    outComputeOGRFullLayerXMLFile =  workspace + "\\" + "OTBClassificationFiles" + "\\" + "{0}_Classification_ComputeOGRFullLayer.xml".format(ortho_name)
#
#    attribute1 = "meanb1"
#    attribute2 = "meanb2"
#    ClassField = 'class'
#    PredictedClass = 'predicted'
#
#    Model = workspace + "\\" + "OTBClassificationFiles" + "\\" + "{0}_Classification_Model.model".format(ortho_name)
#
#    # ---------- OTB Segmentation ---------- #
#
#    otb_seg = otb_segmentation()
#
#    #MeanShiftSmoothing
#    otb_seg.MeanShiftSmoothing(pathToOTB, ortho, outStep1Filter, spatialr, ranger)
#
#    #LSMSSegmentation
#    otb_seg.LSMSSegmentation(pathToOTB, outStep1Filter, outStep2, spatialr, ranger, workspace + "\\" + "Temp")
#
#    # LSMSSmallRegionsMerging
#    otb_seg.LSMSSmallRegionsMerging(pathToOTB, ortho, outStep2, outStep3, minSize)
#
#    # LSMSVectorization
#    otb_seg.LSMSVectorization(pathToOTB, ortho, outStep3, outStep4)

    # ---------- GRASS ----------#

    grass = grass_api(grassPath,dbPath,location,mapset)

    #grass.import_file()

    #
    # # import each map and prepare string of names
    # files_name = glob.glob(folderPathLASClassification + "\*.tif")
    # merge_maps_name = ""
    # i = 0
    # for file in files_name:
    #     grass.import_file(file, mapName+str(i))
    #     merge_maps_name += ("," + mapName+str(i))
    #     i+=1
    # merge_maps_name = merge_maps_name[1:]
    #
    # #GRASS - Region
    # print "SetRegion"
    # grass.region_on_map(merge_maps_name)
    #
    # #GRASS - Merge
    # print "Merge"
    # grass.merge_img(merge_maps_name, mapName + "Merge")
    # mapName = mapName + "Merge"
    #
    # #GRASS - Resample
    # print "Resample"
    # grass.resample(mapName,mapName + "Resample",0.2)
    # mapName = mapName + "Resample"
    #
    # #GRASS - Resample Null
    # print "replaceNull"
    # grass.replace_null(mapName, 3)
    #
    # #GRASS - Reclass
    # print "Reclass"
    # grass.reclass(mapName,mapName + "Reclass", ruleFile)
    # mapName = mapName + "Reclass"
    #
    # #GRASS - Export Raster
    # print "ExportRaster"
    # grass.export_raster(mapName,ExportRasterGrass, 'Byte')
    #
    # # ---------- QGIS --------- #
    #
    # qgis = qgis_api()
    #
    # qgis.remove_attribute_if_exists(outStep4,'_Majority')
    #
    # qgis.remove_attribute_if_exists(outStep4,'_Mean')
    #
    # #QGIS - Statistique Majorité
    # qgis.zonal_stat(outStep4, ExportRasterGrass)
    #
    # #QGIS - Statistique Moyenne
    # qgis.zonal_stat(outStep4, DEMFile, "mean")
    #
    # # Lowercase attributes
    # qgis.lowercase_attribute(outStep4)
    #
    # # Select features - Arbre
    # qgis.feature_selection_export(outStep4,'_Majority = 1', exportArbre)
    #
    # # Select features - Bâtiment
    # qgis.feature_selection_export(outStep4,'_Majority = 2', exportBatiment)
    #
    # # Select features - Arbuste
    # qgis.feature_selection_export(outStep4,'_Majority = 3 and _Mean >= 0,5', exportArbuste)
    #
    # # Select features - Sol (tout le reste)
    # qgis.feature_selection_export(outStep4,'_Majority = 3 and _Mean < 0,5', exportSol)
    #
    # # Remove attribute if exists
    # qgis.remove_attribute_if_exists(exportSol,'traincla')
    #
    # # Add attribute
    # qgis.add_training_attribute(exportSol,'traincla')
    #
    # # Set features of attribute to 0
    # qgis.set_attribute_to_value(exportSol, 'traincla', 0)
    #
    # #To set Training Sites manually in QGIS
    # pause()
    #
    # qgis.feature_selection_export(exportSol, "traincla != 0", TrainingSites)
    #
    # # Remove Predicted attribute if exists before classification
    # qgis.remove_attribute_if_exists(exportSol,"predicted")
    #
    # # ---------- OTB classification ---------- #
    #
    # otb_classif = otb_classification()
    #
    # #ComputeOGRLayersFeaturesStatistics
    # otb_classif.ComputeOGRLayersFeaturesStatistics(pathToOTB, TrainingSites,outComputeOGRTrainingLayerXMLFile, attribute1, attribute2)
    # otb_classif.ComputeOGRLayersFeaturesStatistics(pathToOTB, exportSol,outComputeOGRFullLayerXMLFile, attribute1, attribute2)
    #
    # #TrainOGRLayersClassifier
    # otb_classif.TrainOGRLayersClassifier(pathToOTB, TrainingSites, outComputeOGRTrainingLayerXMLFile, Model, attribute1, attribute2, ClassField )
    #
    # #OGRLayerClassifier
    # otb_classif.OGRLayerClassifier (pathToOTB, exportSol, outComputeOGRFullLayerXMLFile, Model, attribute1, attribute2, PredictedClass)
    #
    #
    # # ---------- QGIS ---------- #
    #
    # # Add predicted attribute
    # qgis.add_training_attribute(exportArbre,'predicted')
    # qgis.add_training_attribute(exportBatiment,'predicted')
    # qgis.add_training_attribute(exportArbuste,'predicted')
    #
    # qgis.set_attribute_to_value(exportArbre, 'predicted', 8)
    # qgis.set_attribute_to_value(exportBatiment, 'predicted', 4)
    # qgis.set_attribute_to_value(exportArbuste, 'predicted', 9)
    #
    # #change shadow value to water value (6 to 1)
    # set_shadow_to_water(exportSol, 'predicted')

if __name__ == "__main__":
    main()