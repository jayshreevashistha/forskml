# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:39:03 2019

@author: computer
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("breast_cancer.csv")

for i in dataset:
    dataset[i] = dataset[i].fillna(dataset[i].mode()[0])


features = dataset.iloc[:, 1:10].values
labels = dataset.iloc[:, 10].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("cm:",cm)
Score = classifier.score(features_test,labels_test)
print("Score:",Score)



x=[6,2,5,3,2,7,9,2,4]
x=np.array(x).reshape(1,-1)
print("Class: ",classifier.predict(x))



if ("class[4]"):
    print("Cancerous")
else:
    print("Not Cancerous")