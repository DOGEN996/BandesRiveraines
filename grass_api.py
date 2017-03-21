# -*- coding: utf-8 -*-

from cmd_executer import cmd_executer

class grass_api(cmd_executer):

    header = ""

    def __init__(self,grass_path,db_path,location,mapset):
        self.header = grass_path + " " + db_path + '\\' + location + '\\' + mapset + '\\'
    
    def import_file(self,file_name, output_name):
        self.execute("%s --exec r.in.gdal -o --o --v input=%s output=%s"%(self.header,file_name,output_name))

    def region_on_map(self,map_name):
        self.execute("%s --exec g.region raster=%s -p"%(self.header,map_name))
    
    def region_res(self,res):
        self.execute("%s --exec g.region res=%f -ap"%(self.header,res))
    
    def export_raster(self,map_name,output_name,data_type):
        self.region_on_map(map_name)
        self.execute("%s --exec r.out.gdal --o --v input=%s output=%s type=%s"%(self.header,map_name,output_name,data_type))
    
    def replace_null(self,map_name,replace_num):
        self.execute("%s --exec r.null --v map=%s null=%d"%(self.header,map_name,replace_num))
    
    def reclass(self,map_name,output_name,rules_file):
        self.execute("%s --exec r.reclass --o --v input=%s output=%s rules=%s"%(self.header,map_name,output_name,rules_file))
    
    def resample(self,map_name, output_name, final_res):
        self.region_on_map(map_name)
        self.region_res(final_res)
        self.execute("%s --exec r.resample --o --v input=%s output=%s"%(self.header,map_name,output_name))
    
    def merge_img(self,input_maps_string, output_name):
        self.execute("%s --exec r.patch --o --v input=%s output=%s"%(self.header,input_maps_string,output_name))

    ## Ajout de Dom Pour erosion


    def fill_dir(self, input_dem, output_dem, direction):
        self.region_on_map(input_dem)
        self.execute("%s --exec r.fill.dir --o --v input=%s output=%s direction=%s"%(self.header,input_dem,output_dem,direction))

    def fill_nulls(self, input_dem, output_dem):
        self.execute("%s --exec r.fillnulls --o --v input=%s output=%s method=rst"%(self.header,input_dem,output_dem))

    #def watershed(self, input_dem, output_drainage, output_basin, output_stream, threshold  ):
    #    self.region_on_map(input_dem)
    #    self.execute("%s --exec r.watershed --o --v -s input=%s drainage=%s basin=%s stream=%s thresh=%s"%(self.header,input_dem,output_drainage, output_basin, output_stream, threshold))

    def stream_extract(self, input_dem, threshold, stream_raster, stream_vector):
        self.execute("%s --exec r.stream.extract --0 --v elevation=%s threshold=%s d8cut=0 memory=8000 stream_raster=%s stream_vector=%s"%(self.header,input_dem,threshold,stream_raster,stream_vector))

    # def to_vect(self, input, output, type):
    #    self.execute("%s --exec r.to.vect --o --v input=%s output=%s type=%s"%(self.header,input,output,type))

    #def export_vector(self, input_vector, type,):




















