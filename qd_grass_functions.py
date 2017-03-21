# -*- coding: utf-8 -*-

from cmd_executer import cmd_executer

class qd_grass(cmd_executer):

    header = ""
    grass_path = ""
    workspace = ""

    def __init__(self,grass_path,db_path,location,mapset):
        self.workspace = db_path + '\\' + location + '\\'
        self.header = grass_path + " " + self.workspace + mapset + '\\'
        self.grass_path = grass_path


    def loc_from_file(self,file_path):
        self.execute("%s -c %s %s"%(self.grass_path,file_path,self.workspace))

    def import_file(self,file_name, output_name):
        self.execute("%s --exec r.in.gdal -o --o --v input=%s output=%s"%(self.header,file_name,output_name))

    def region_on_map(self,map_name):
        self.execute("%s --exec g.region raster=%s -p"%(self.header,map_name))

    def fill_dir(self, input_dem, output_dem, direction):
        self.region_on_map(input_dem)
        self.execute("%s --exec r.fill.dir --o --v input=%s output=%s direction=%s"%(self.header,input_dem,output_dem,direction))

    def fill_nulls(self, input_dem, output_dem):
        self.region_on_map(input_dem)
        self.execute("%s --exec r.fillnulls --o --v input=%s output=%s method=rst"%(self.header,input_dem,output_dem))

    #def watershed(self, input_dem, output_drainage, output_basin, output_stream, threshold  ):
    #    self.region_on_map(input_dem)
    #    self.execute("%s --exec r.watershed --o --v -s input=%s drainage=%s basin=%s stream=%s thresh=%s"%(self.header,input_dem,output_drainage, output_basin, output_stream, threshold))

    def stream_extract(self, input_dem, threshold, stream_raster, stream_vector):
        self.execute("%s --exec r.stream.extract --0 --v elevation=%s threshold=%s d8cut=0 memory=8000 stream_raster=%s stream_vector=%s"%(self.header,input_dem,threshold,stream_raster,stream_vector))
