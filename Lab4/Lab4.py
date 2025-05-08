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
excluded_states = {'AK', 'HI', 'PR', 'GU', 'VI', 'MP', 'AS','DC'}

#filter using this set
geoData = geoData[~geoData['STUSPS'].isin(excluded_states)]

#dissolve to create state boundaries
states = geoData.dissolve(by='STUSPS', as_index=False, aggfunc='first')


#Visualize the Map of the United States
def baseMap():
    fig, ax = plt.subplots(figsize=(8, 5))
    states.plot(ax=ax, edgecolor='black', cmap='Pastel1')
    ax.set_title("Base Map of 48 Contiguous United States", fontsize=20)

    #turn off axis and tighten layout
    ax.axis('off')
    plt.tight_layout()

    # Save before show
    fig.savefig('Boyce_baseMap.png')
    plt.show()

    print("baseMap Generated")



#Visualize the Distribution of geographic data
def geoMap():
    fig = plt.figure(1, figsize=(20, 10))
    ax = fig.add_subplot()
    ax.set_title("Map of 48 Contiguous United States with Geographic Data", fontsize=20)

    #plot the state names
    states.apply(lambda x: ax.annotate(x.STUSPS, xy=x.geometry.centroid.coords[0], ha='center', fontsize=14), axis=1)

    #plot the state boundaries
    states.boundary.plot(ax=ax, color='Red', linewidth=.6)

    #plot the states
    states.plot(ax=ax, cmap='Pastel2')

    #turn off axis and tighten layout
    ax.axis('off')
    plt.tight_layout()

    #legend text box
    key_text = "\n".join([f"{abbr} — {name}" for abbr, name in zip(states['STUSPS'], states['STATE_NAME'])])

    #debug
    print(key_text)

    props = dict(boxstyle='round', facecolor='white', alpha=0.8)
    ax.text(0.95, 0.5, key_text, transform=ax.transAxes, fontsize=12, verticalalignment='center', bbox=props, family='monospace')

    plt.show()
    fig.savefig('Boyce_geoMap.png')     # save the map as a png file
    print("geoMap Generated")

'''Generate Five Representative and Unique Statistical Results:
Select any five meaningful statistics or insights from the dataset. These could be:
The total number of tornadoes per state.
Any other insightful measure derived from the data.
Present these statistical results through appropriate visualizations (e.g., bar charts,
line graphs, histograms, or box plots).
Ensure that each visualization is clearly labeled and includes an interpretation of
the results'''


baseMap() #Visualize the Map of the United States
geoMap()  #Visualize the Distribution of geographic data


