# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:49:06 2019

@author: computer
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat',delimiter=" ")

#prepare the data to train the model
features = dataset.iloc[:,:-1].values  
labels = dataset.iloc[:, 8].values 

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train) 
#Predict on test and training data

predict_test_lm =regressor.predict(features_test )  
from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lm),2) )

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
regressor_lasso = Lasso() 
regressor_ridge =  Ridge() 
regressor_lasso.fit(features_train, labels_train)
regressor_ridge.fit(features_train, labels_train)


predict_test_lasso = regressor_lasso.predict (features_test) 
predict_test_ridge = regressor_ridge.predict (features_test)

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))




#predict whether lpsa is high or low, from other variables


df= pd.read_csv('http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat',delimiter=" ")
df["lpsa"] = dataset["lpsa"].map(lambda x: True if x>2.5 else False, range(1, 10))


#prepare the data to train the model
features = df.iloc[:,:-1].values  
labels = df.iloc[:, 8].values 
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("cm:",cm)
Score = classifier.score(features_test,labels_test)
print("Score:",Score)