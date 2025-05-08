#Lab4.py

import geopandas
import matplotlib.pyplot as plt
import warnings
from collections import Counter

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

#Land Area per State Bar Chart
#barchart showing total land area per state
def landArea():
    #convert to square kilometers
    state_land = geoData.groupby('STATE_NAME')['ALAND'].sum() / 1e6
    #sort values
    state_land = state_land.sort_values(ascending=False)

    #plot setup
    state_land.plot(kind='bar', figsize=(14, 6), color='seagreen')
    plt.title('Total Land Area per State (sq km)')
    plt.ylabel('Land Area (km²)')
    plt.xlabel('State')
    plt.xticks(rotation=90)
    plt.tight_layout()

    #save the plot as a png file
    plt.savefig('Boyce_landArea.png')
    plt.show()
    print("Total Land Area per State")

#Top 10 States by Water Area
#barchart showing states with the most water
def top10water():
    #convert to square kilometers
    state_water = geoData.groupby('STATE_NAME')['AWATER'].sum() / 1e6
    #sort values
    top10 = state_water.sort_values(ascending=False).head(10)

    #plot setup
    top10.plot(kind='barh', figsize=(10, 6), color='steelblue')
    plt.title('Top 10 States by Total Water Area (sq km)')
    plt.xlabel('Total Water Area (km²)')
    plt.tight_layout()

    #save the plot as a png file
    plt.savefig('Boyce_top10water.png')
    plt.show()
    print("Top 10 States by Water Area")


#Vowel Count per State Name
#barchart showing states with the most vowels
def vowel_count():

    #count vowels in a state name
    def count_vowels(name):
        return sum(1 for c in name.lower() if c in 'aeiou')

    #get unique state names
    unique_states = geoData['STATE_NAME'].drop_duplicates()

    #list of (state, vowel_count) tuples
    state_vowel_counts = [(state, count_vowels(state)) for state in unique_states]

    #sort by vowel count
    state_vowel_counts.sort(key=lambda x: x[1], reverse=True)

    #convert to lists for plotting
    states, counts = zip(*state_vowel_counts)

    #plot setup
    plt.figure(figsize=(12, 6))
    plt.bar(states, counts, color='purple')
    plt.title('Number of Vowels in Each State Name')
    plt.xlabel('State')
    plt.ylabel('Vowel Count')
    plt.xticks(rotation=45)
    plt.tight_layout()

    #save the plot as a png file
    plt.savefig('Boyce_vowel_counts.png')
    plt.show()
    print("States by Vowel Count")


#Most Common Starting Letters in State Names
#barchart showing the most common starting letters in state names
def starting_letters():
    #get the first letter of each unique state name
    initials = geoData['STATE_NAME'].drop_duplicates().str[0].str.upper()
    initial_counts = Counter(initials)

    #convert to sorted lists for plotting
    letters, counts = zip(*sorted(initial_counts.items(), key=lambda x: x[1], reverse=True))

    #plot setup
    plt.figure(figsize=(10, 5))
    plt.bar(letters, counts, color='darkorange')
    plt.title('Most Common Starting Letters in State Names')
    plt.xlabel('Starting Letter')
    plt.ylabel('Number of States')
    plt.tight_layout()

    #save the plot as a png file
    plt.savefig('Boyce_letters.png')
    plt.show()
    print("Most Common Starting Letters")


#Land vs. Water Area by State
#barchart showing land vs. water area by state
def land_vs_water():
    import numpy as np

    #aggregate land and water area by state
    area_by_state = geoData.groupby('STATE_NAME')[['ALAND', 'AWATER']].sum()

    #convert to square kilometers
    area_by_state_km2 = area_by_state / 1e6

    #plot setup
    states = area_by_state_km2.index
    x = np.arange(len(states))
    width = 0.4

    plt.figure(figsize=(16, 8))
    plt.bar(x - width/2, area_by_state_km2['ALAND'], width, label='Land Area (km²)', color='forestgreen')
    plt.bar(x + width/2, area_by_state_km2['AWATER'], width, label='Water Area (km²)', color='royalblue')

    plt.xlabel('State')
    plt.ylabel('Area (in km²)')
    plt.title('Land vs. Water Area by State')
    plt.xticks(x, states, rotation=90)
    plt.legend()
    plt.tight_layout()

    #save the plot as a png file
    plt.savefig('Boyce_land_vs_water.png')
    plt.show()
    print("Land vs. Water Area by State")



baseMap() #Visualize the Map of the United States
geoMap()  #Visualize the Distribution of geographic data

landArea()  #1
top10water()  #2
vowel_count() #3
starting_letters()  #4
land_vs_water() #5
