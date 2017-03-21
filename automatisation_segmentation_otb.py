#
import subprocess
import os


class otb_segmentation:

    # Step 1
    def MeanShiftSmoothing(self,pathToOTB, orthophoto, outStep1Filter, spatialr, ranger):
        print "Segmentation Step 1 ... "
        path = pathToOTB + "\\" + "otbcli_MeanShiftSmoothing.bat"
        print path
        subprocess.call([path, "-in",orthophoto,"-fout",outStep1Filter,"-spatialr",str(spatialr),"-ranger",str(ranger),"-thres","0.1","-maxiter","100"])

    # Step 2
    def LSMSSegmentation(self, pathToOTB,Step1Filter, outStep2, spatialr, ranger, temp_directory):
        print "Segmentation Step 2 ... "
        path = pathToOTB + "\\" + "otbcli_LSMSSegmentation.bat"
        subprocess.call([path, "-in",Step1Filter,"-out",outStep2,"-spatialr",str(spatialr),"-ranger",str(ranger), "-minsize","0","-tilesizex","500","-tilesizey","500", "-tmpdir", temp_directory ])

    # Step 3
    def LSMSSmallRegionsMerging(self, pathToOTB, orthophoto, Step2, outStep3, minSize):
        print "Segmentation Step 3 ... "
        path = pathToOTB + "\\" + "otbcli_LSMSSmallRegionsMerging.bat"
        subprocess.call([path, "-in",orthophoto,"-inseg",Step2, "-out",outStep3,"-minsize",str(minSize),"-tilesizex","500","-tilesizey","500"])

    # Step 4
    def LSMSVectorization(self, pathToOTB, orthophoto, Step3, outStep4):
        print "Segmentation Step 4 ... "
        path = pathToOTB + "\\" + "otbcli_LSMSVectorization.bat"
        subprocess.call([path, "-in",orthophoto,"-inseg",Step3,"-out",outStep4,"-tilesizex", "500", "-tilesizey","500"])

    # Remove file
    def remove_file(self, file_to_remove):
        print "removing tempory files ... "
        os.remove(file_to_remove)
