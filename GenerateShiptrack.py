import xarray as xr
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import LineString
#import fiona
from fiona.crs import from_epsg

ds = xr.open_dataset('/Volumes/MNF-Archive/underway/in2019_v04uwy.nc')

newdata = gpd.GeoDataFrame()
newdata['geometry'] = None

coordinates = zip(ds.longitude.data[::100][1:],ds.latitude.data[::100][1:])

poly = LineString(coordinates)

newdata.loc[0, 'geometry'] = poly

newdata.crs = from_epsg(4326)

newdata.to_file('CurrentShiptrack.shp')



