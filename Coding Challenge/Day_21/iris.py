# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:45:30 2019

@author: computer
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets 
iris = datasets.load_iris()

features= pd.DataFrame(iris.data, columns= iris.feature_names )
labels = iris.target

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

# kernels: linear, poly and rbf
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("cm:",cm)

# Model Score
score = classifier.score(features_test,labels_test)
print("Score:",score)