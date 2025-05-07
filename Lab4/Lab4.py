#Lab4.py


import geopandas
import matplotlib.pyplot as plt

states = geopandas.read_file('cb_2020_us_cousub_500k.shp')

states.head()
