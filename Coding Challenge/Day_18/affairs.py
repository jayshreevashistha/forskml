# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:14:14 2019

@author: computer
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('affairs.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, 8].values

# Encoding categorical data
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features =[6])
features = onehotencoder.fit_transform(features).toarray()
# dropping first column
features = features[:, 1:]

# Encoding categorical data
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features =[11])
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
print(cm)

Score = classifier.score(features_train, labels_train)
Score = classifier.score(features_test, labels_test)
print(Score)

#data_gender_ref['Male'] = [data_gender['sex'][0]]

data=dataset['affair'].value_counts(normalize = True)[1] 
print("percentage",data)
# She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.

x=[1,0,0,0,0,0,0,0,1,0,3,25,3,1,4,17]
x=np.array(x).reshape(1,-1)
print("Affair:",classifier.predict(x))