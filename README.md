# Windows only

## cannot work on Ubuntu

pip install GDAL-3.3.0-cp310-cp310-win_amd64.whl

git clone https://github.com/roelderickx/ogr2osm.git
cd ogr2osm
python setup.py install
cd ..

python erase.py input_name.osm mask_name.geojson output_name.osm