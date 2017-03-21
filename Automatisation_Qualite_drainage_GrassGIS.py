import os
import sys
import csv
import subprocess
import shlex


#path

#
#
#outlet_file = 'E:\Etude\APP\Qualite_drainage\ProjetAPP\outlets_br.csv'
#
#rows = list(open(outlet_file))
#
#totalrows = len(rows) - 1
#
GrassGisPath = r"E:\GRASS GIS 7.2.0\bin"



os.chdir(GrassGisPath)




def execute(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()
    rc = process.poll()
    return rc

cmd = "g.region raster=DEM_filled@Do"
execute(cmd)


##execute(os.path.join(GrassGisPath,"g.region")+" raster=DEM_filled@Do")
#
##loop through the csv(coordinates) file in r.water.outlet module
#f = open(outlet_file, 'r')
#element = list(csv.reader(f))
#i = 0
#j = 0
#while True:
#    if i <= totalrows:
#        east = element[i][j]
#        north = element[i][j + 1]
#
#        #execute([os.path.join(GrassGisPath,"r.water.outlet"),'input=drainagedir@Do', 'output=wshed_{0}@Do'.format(str(i+1)), 'coordinates={0},{1}'.format(east,north)])
#        #execute([os.path.join(GrassGisPath,"r.null"),"-q","map=wshed_{0}@Do".format(i),"setnull=0"])
#        #execute([os.path.join(GrassGisPath,"r.to.vect"),"-s", "input=wshed_{0}@Do".format(i),"output=wshed_{0}@Do".format(i),"type=area"])
#        #execute([os.path.join(GrassGisPath,"g.remove"),"type=rast","name=wshed_{0}@Do".format(i)])
#
#        #subprocess.call([os.path.join(GrassGisPath,"r.water.outlet"),'input=drainagedir@Do', 'output=wshed_{0}@Do'.format(str(i+1)), 'coordinates={0},{1}'.format(east,north)])
#        #subprocess.call([os.path.join(GrassGisPath,"r.null"),"-q","map=wshed_{0}@Do".format(i),"setnull=0"])
#        #subprocess.call([os.path.join(GrassGisPath,"r.to.vect"),"-s", "input=wshed_{0}@Do".format(i),"output=wshed_{0}@Do".format(i),"type=area"])
#        #subprocess.call([os.path.join(GrassGisPath,"g.remove"),"type=rast","name=wshed_{0}@Do".format(i)])
#
#        i = i + 1
#    else:
#        print "created {0} catchments".format(i)
#        break
#
#print "Patching and cleaning up watersheds ..."
#
##subprocess.call([os.path.join(GrassGisPath,"v.patch"), "input=`g.mlist", "vect", "pattern=wshed_*@Do","separator=,`", "out=wshed_patch@Do"])
#
##subprocess.call([os.path.join(GrassGisPath,"v.clean"), "wshed_patch@Do", "out=wshed_clean@Do", "tool=snap,rmdupl","thresh=20"])
#
##subprocess.call([os.path.join(GrassGisPath,"v.category"), "in=wshed_clean@Do", "out=wshed_clean2@Do", "opt=del"])
#
##subprocess.call([os.path.join(GrassGisPath,"v.category"), "in=wshed_clean2@Do", "out=wshed_final@Do", "type=centroid","opt=add"])
#
##subprocess.call([os.path.join(GrassGisPath,"g.remove"), "vect=wshed_clean@Do,wshed_clean2@Do"])
#
##print "Calculating area for watersheds ..."
#
##subprocess.call([os.path.join(GrassGisPath,"v.db.addtable"), "map=wshed_final", "columns='area_sqkm DOUBLE PRECISION'"])
#
##subprocess.call([os.path.join(GrassGisPath,"v.to.db"), "map=wshed_final", "option=area","col=area_sqkm", "unit=k"])
#
#print "viewer ..."
#
##subprocess.call([os.path.join(GrassGisPath,"d.vect"),"wshed_final@Do","type=boundary,centroid","display=shape", "size=0","width=3","color=orange"])
#
#