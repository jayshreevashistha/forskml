# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:12:31 2019

@author: computer
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data.csv')

# Filling out the nan values with 'Mising' keyword
#dataset = dataset.replace(np.nan, 'Mising')


df = dataset['Country'].dropna().value_counts()
x = df.index
y = df.values

patches, texts = plt.pie(y,shadow=True, startangle=90)
plt.legend(patches, x, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()


#Visualize the various countries from where the artworks are coming
dataset['Country'].dropna().value_counts().plot.pie()

#Visualize the top 2 classification for the artworks
dataset['Classification'].dropna().value_counts()[:2].plot.bar()

#Visualize the artist interested in the artworks
dataset['Artist Display Name'].dropna().value_counts()[:10].plot.bar()

#Visualize the top 2 culture for the artworks
dataset['Culture'].dropna().value_counts()[:2].plot.bar()