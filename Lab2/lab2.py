#lab2.py
#visualizing Real Data Sets using Seaborn
#Generate five meaningful and unique visualizations using Seaborn
#Save each visualization as an image file boyce-bargraph.png


#Data files:
#default of credit card clients.csv
#https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea

#global dataset variable
df = pd.read_csv('default of credit card clients.csv', delimiter=';')  # open the dataset



#explain the data
def explain_data():
    print("\n"
          "Sourced from UCI Machine Learning Repository\n"
          )


#Print a portion of the raw data using head()
def print_data_head():
    #read the dataset
    print(df.head()) #print the head

#seaborn


explain_data()
print_data_head()

