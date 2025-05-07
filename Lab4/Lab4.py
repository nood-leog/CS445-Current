#Lab4.py

import geopandas
import matplotlib.pyplot as plt
import warnings

#ignore warnings
warnings.filterwarnings("ignore", category=UserWarning, append=True)
warnings.filterwarnings("ignore", category=RuntimeWarning, append=True)

#read cb_2020_us_cousub_500k.shp
geoData = geopandas.read_file('cb_2020_us_cousub_500k.shp')

#print head
print(geoData.head())

#print column names
print(geoData.columns)

#print the crs set in the data file
print("Current crs:", geoData.crs)
#reproject it's coordinates to Mercator
geoData = geoData.to_crs("EPSG:3395")
#print the new crs
print("Set crs to:", geoData.crs)

#exclude non-contiguous states
excluded_states = {'AK', 'HI', 'PR', 'GU', 'VI', 'MP', 'AS'}

#filter using this set
geoData = geoData[~geoData['STUSPS'].isin(excluded_states)]

#dissolve to create state boundaries
states = geoData.dissolve(by='STUSPS')

# Plot the map
states.plot(edgecolor='black', figsize=(12, 8))
plt.title("Contiguous United States (from County Subdivisions)")
plt.axis("off")
plt.show()

