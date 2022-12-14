# -*- coding: utf-8 -*-
"""Portfolio Project Dataset (Piracy).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nritI4RDFO4BevtassX0iyU31mNcfEgl
"""

pip install geopandas

#packages
pip install geopandas
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from datetime import datetime
from shapely import geometry
from shapely.geometry import Point
import matplotlib.pyplot as plt

#load data, tidy data, removed columns & NaN values, reset index.
pirate = pd.read_csv('/content/drive/MyDrive/pirate_attacks.csv')

pirate_list = list(pirate)
pirate = pirate.drop(['time','location_description',
                      'attack_type','nearest_country','eez_country','data_source',
                      'shore_distance','shore_longitude','shore_latitude',
                      'attack_description','vessel_name','vessel_type','vessel_status'],
                     axis=1)

pirate["date"] = pd.to_datetime(pirate["date"]) 

pirate.fillna(0,inplace=True)
pirate.reset_index(drop=True, inplace=True)

import plotly.express as px

fig = px.scatter_geo(pirate,lat='latitude',lon='longitude', hover_name="date")
fig.update_layout(title = 'Global Piracy, 1993-2020', title_x=0.5)
fig.show()

geometry = [Point(xy) for xy in zip(pirate["longitude"], pirate["latitude"])]
gdf = GeoDataFrame(pirate, geometry=geometry)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(15, 15)), marker='o', color='red', markersize=15);

pirate = pirate.drop(['longitude','latitude'],axis=1)

fig, ax = plt.subplots()

# Plot a histogram of Parasleep from the Sleep DataFrame
ax.hist(pirate['date'])

# Specify the axis labels and plot title
ax.set_xlabel('Date')
ax.set_ylabel('Frequency of Attacks') 
ax.set_title('Global Pirate Attacks from 1993-2020') 

plt.show()
