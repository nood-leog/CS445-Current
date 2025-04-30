#Lab3.py
# visualizing Real Data Sets using Seaborn

# Data files:
# winequality-red.csv

import pandas as pd
import plotly.express as px


# ignore future warnings =
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

# global dataset variable
df = pd.read_csv('winequality-red.csv')

# explain the data
def explain_data():
    print("\n"
          "This dataset contains information about red wine quality.\n"
          "It includes all information about the wine, including chemical properties and quality rating.\n"
          "The dataset contains 11 features in total:\n"
          "fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality\n"

          "Sourced from https://github.com/plotly/datasets/blob/master/winequality-red.csv\n"
          )


# Print a portion of the raw data using head()
def print_data_head():
    # read the dataset
    print(df.head())
    print("\nColumn names:\n", df.columns.tolist(), "\n")

# 1
def fixed_volatile_quality():
    fig = px.scatter_3d(df,
                        x='fixed acidity',
                        y='volatile acidity',
                        z='quality',
                        color='quality',
                        title='Fixed Acidity vs Volatile Acidity vs Quality')
    fig.update_layout(scene_camera=dict(eye=dict(x=0, y=0, z=2)))  # top-down
    fig.show()

# 2
def alcohol_sulphates_quality():
    fig = px.scatter_3d(df,
                        x='alcohol',
                        y='sulphates',
                        z='quality',
                        color='quality',
                        title='Alcohol vs Sulphates vs Quality')
    fig.update_layout(scene_camera=dict(eye=dict(x=0, y=0, z=2)))
    fig.show()

# 3
def citric_ph_quality():
    fig = px.scatter_3d(df,
                        x='citric acid',
                        y='pH',
                        z='quality',
                        color='quality',
                        title='Citric Acid vs pH vs Quality')
    fig.update_layout(scene_camera=dict(eye=dict(x=0, y=0, z=2)))
    fig.show()



# 4
def so2_totalso2_quality():
    fig = px.scatter_3d(df,
                        x='free sulfur dioxide',
                        y='total sulfur dioxide',
                        z='quality',
                        color='quality',
                        title='Free SO₂ vs Total SO₂ vs Quality')
    fig.update_layout(scene_camera=dict(eye=dict(x=0, y=0, z=2)))
    fig.show()


# 5
def density_sugar_quality():
    fig = px.scatter_3d(df,
                        x='density',
                        y='residual sugar',
                        z='quality',
                        color='quality',
                        title='Density vs Residual Sugar vs Quality')
    fig.update_layout(scene_camera=dict(eye=dict(x=0, y=0, z=2)))
    fig.show()

explain_data()
print_data_head()

fixed_volatile_quality() #1
alcohol_sulphates_quality() #2
citric_ph_quality() #3
so2_totalso2_quality() #4
density_sugar_quality() #5