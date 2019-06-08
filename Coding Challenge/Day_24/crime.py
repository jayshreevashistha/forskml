# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:27:44 2019

@author: computer
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans


# Importing the dataset
dataset = pd.read_csv('crime_data.csv')
dataset= dataset.drop(['State','UrbanPop'],axis=1)
features = dataset.iloc[:,:].values

from sklearn.model_selection import train_test_split
features_train, features_test = train_test_split(features,test_size = 0.2, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

#Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)
explained_variance = pca.explained_variance_ratio_


# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

# Visualising the clusters
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'low crime')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Medium crime')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'High Crime')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()



