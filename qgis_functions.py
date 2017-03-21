# -*- coding: utf-8 -*-

from qgis.core import *
from PyQt4.QtCore import QVariant
from qgis.analysis import QgsZonalStatistics



class qgis_api:

    polygonLayer = None

    def __init__(self):
        QgsApplication.setPrefixPath(r"C:\OSGeo4W64\bin", True)
        qgis = QgsApplication([], False)
        qgis.initQgis()


    def remove_attribute_if_exists (self,vector_file,attribute_name):
        polygonLayer = QgsVectorLayer(vector_file, 'zonepolygons', 'ogr')
        caps = polygonLayer.dataProvider().capabilities()
        ind = polygonLayer.dataProvider().fieldNameIndex(attribute_name)
        if ind != -1:
            if caps & QgsVectorDataProvider.DeleteAttributes:
                res = polygonLayer.dataProvider().deleteAttributes([ind])


    def zonal_stat(self, vector_file,raster_file_name, stat_type = "Majority"):
        polygonLayer = QgsVectorLayer(vector_file, 'zonepolygons', 'ogr')
        zoneStat = ''
        if stat_type == "mean":

            zoneStat = QgsZonalStatistics (polygonLayer, raster_file_name, '_', 1,QgsZonalStatistics.Mean)

        else:
            zoneStat = QgsZonalStatistics (polygonLayer, raster_file_name, '_', 1,QgsZonalStatistics.Majority)

        zoneStat.calculateStatistics(None)

    def feature_selection_export(self,vector_file,expression, path_expression_result):
        polygonLayer = QgsVectorLayer(vector_file, 'zonepolygons', 'ogr')
        exp = QgsExpression(expression)
        selection = polygonLayer.getFeatures(QgsFeatureRequest(exp))
        ids = [i.id() for i in selection]
        polygonLayer.setSelectedFeatures(ids)
        QgsVectorFileWriter.writeAsVectorFormat(polygonLayer,path_expression_result,'utf-8',None,'ESRI Shapefile',True)

    def lowercase_attribute(self, vector_file):
        polygonLayer = QgsVectorLayer(vector_file, 'zonepolygons', 'ogr')
        k = 0
        fields = polygonLayer.pendingFields()
        polygonLayer.startEditing()
        for (field) in fields:
            polygonLayer.renameAttribute(k, field.name().lower())
            k  += 1
        polygonLayer.commitChanges()

    def set_attribute_to_value(self, vector_file, field, int_value):
        polygonLayer = QgsVectorLayer(vector_file, 'zonepolygons', 'ogr')
        polygonLayer.startEditing()
        index = polygonLayer.fieldNameIndex(field)
        for feature in polygonLayer.getFeatures():
            polygonLayer.changeAttributeValue(feature.id(), index, int_value)
        polygonLayer.commitChanges()

    def set_shadow_to_water(self, vector_file, field):
        polygonLayer = QgsVectorLayer(vector_file, 'zonepolygons', 'ogr')
        polygonLayer.startEditing()
        index = polygonLayer.fieldNameIndex(field)
        for feature in polygonLayer.getFeatures():
            if feature[field] == 6:
                polygonLayer.changeAttributeValue(feature.id(), index, 1)
        polygonLayer.commitChanges()

    def add_training_attribute(self,vector_file,training_class_field):
        polygonLayer = QgsVectorLayer(vector_file, 'zonepolygons', 'ogr')
        polygonLayer.startEditing()
        caps = polygonLayer.dataProvider().capabilities()
        if caps & QgsVectorDataProvider.AddAttributes:
            polygonLayer.dataProvider().addAttributes([QgsField(training_class_field, QVariant.Int)])
            polygonLayer.updateFields()
        polygonLayer.commitChanges()




