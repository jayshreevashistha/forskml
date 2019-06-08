# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:32:31 2019

@author: computer
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('mushrooms.csv')
features = dataset.iloc[:,[5,21,22]].values
labels = dataset.iloc[:, 0].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])
features[:, 1] = labelencoder.fit_transform(features[:, 1])
features[:, 2] = labelencoder.fit_transform(features[:, 2])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features =[0])
features = onehotencoder.fit_transform(features).toarray()
# dropping first column
features = features[:, 1:]


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [9])
features = onehotencoder.fit_transform(features).toarray()
# dropping first column
features = features[:, 1:]

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [14])
features = onehotencoder.fit_transform(features).toarray()
# dropping first column
features = features[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

x=[1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]
x=np.array(x).reshape(1,-1)
print("Class: ",classifier.predict(x))