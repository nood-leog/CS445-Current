#lab2.py
#visualizing Real Data Sets using Seaborn
#Generate five meaningful and unique visualizations using Seaborn
#Save each visualization as an image file boyce-bargraph.png


#Data files:
#car.data - car evaluation data set

#buying	Feature	Categorical	buying price
#maint	Feature	Categorical	price of the maintenance
#doors	Feature	Categorical	number of doors
#persons Feature Categorical capacity in terms of persons to carry
#lug_boot Feature Categorical the size of luggage boot
#safety	Feature	Categorical	estimated safety of the car
#class	Target	Categorical	evaluation level (unacceptable, acceptable, good, very good)

#buying:   vhigh, high, med, low.
#maint:    vhigh, high, med, low.
#doors:    2, 3, 4, 5more.
#persons:  2, 4, more.
#lug_boot: small, med, big.
#safety:   low, med, high.
#class: unacc, acc, good, vgood




import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#global dataset variable
df = pd.read_csv('car.data', delimiter=';')  # open the dataset



#explain the data
def explain_data():
    print("\n"
          "Sourced from UCI Machine Learning Repository\n"
          )


#Print a portion of the raw data using head()
def print_data_head():
    #read the dataset
    print(df.head()) #print the head


explain_data()
print_data_head()

