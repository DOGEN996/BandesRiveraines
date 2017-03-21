# -*- coding: utf-8 -*-
#
import subprocess
import os

class otb_classification:

    # Outil: ComputeOGRLayersFeaturesStatistics
    def ComputeOGRLayersFeaturesStatistics(self, pathToOTB, TrainingShp,outComputeOGRTrainingLayerXMLFile, attribute1, attribute2):
        print "Classification ComputeOGRLayersFeaturesStatistics ... "
        path = pathToOTB + "\\" + "otbcli_ComputeOGRLayersFeaturesStatistics.bat"

        subprocess.call([path, "-inshp",TrainingShp,"-outstats",outComputeOGRTrainingLayerXMLFile,
                 "-feat",attribute1,attribute2])

    # Outil: TrainOGRLayersClassifier
    def TrainOGRLayersClassifier(self, pathToOTB, TrainingShp, outComputeOGRTrainingLayerXMLFile, ModelFile, attribute1, attribute2, ClassField ):
        print "Classification TrainOGRLayersClassifier ... "
        path = pathToOTB + "\\" + "otbcli_TrainOGRLayersClassifier"

        subprocess.call([path, "-inshp",TrainingShp,"-instats",outComputeOGRTrainingLayerXMLFile,
                        "-outsvm",ModelFile, "-feat", attribute1,attribute2, "-cfield", ClassField])

    # Outil: OGRLayerClassifier
    def OGRLayerClassifier(self, pathToOTB, FullSegmentationFile, outComputeOGRFullLayerXMLFile, ModelFile, attribute1, attribute2, PredictedClass):
        print "Classification OGRLayerClassifier... "
        path = pathToOTB + "\\" + "otbcli_OGRLayerClassifier.bat"

        subprocess.call([path, "-inshp",FullSegmentationFile,"-instats",outComputeOGRFullLayerXMLFile,
                        "-insvm",ModelFile,"-feat", attribute1,attribute2, "-cfield", PredictedClass])

    # Remove temporary files
    def remove_file(file_to_remove):
        print "removing tempory files ... "
        os.remove(file_to_remove)


