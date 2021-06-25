from osgeo import ogr
import os
import sys
import ogr2osm

input_osm = sys.argv[1]
mask_geojson = sys.argv[2]
output_osm = sys.argv[3]

ds = ogr.Open(input_osm)
maskDriver = ogr.GetDriverByName('GeoJSON')
mask = maskDriver.Open(mask_geojson, 0)
maskLayer = mask.GetLayer()

outputDriver = ogr.GetDriverByName('KML')
fn = "output.kml"
if os.path.exists(fn):
    outputDriver.DeleteDataSource(fn)
outDS = outputDriver.CreateDataSource(fn)

layer_num = ds.GetLayerCount()
for i in range(layer_num):
    inputLayer = ds.GetLayer(i)
    name = inputLayer.GetName()
    outputLayer = outDS.CreateLayer(name)
    inputLayer.Erase(maskLayer, outputLayer)

f = open("output.kml", "a")
f.write("</Folder></Document></kml>")
f.close()

# with open('output.kml', 'a') as output:
#    output.write('</Folder></Document></kml>')

translation_object = ogr2osm.TranslationBase()
datasource = ogr2osm.OgrDatasource(translation_object)
datasource.open_datasource("output.kml")
osmdata = ogr2osm.OsmData(translation_object)
osmdata.process(datasource)
datawriter = ogr2osm.OsmDataWriter(output_osm)
osmdata.output(datawriter)

os.remove('output.kml')

