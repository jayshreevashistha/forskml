# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:51:07 2019

@author: computer
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("bluegills.csv")
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,1].values
plt.scatter(features, labels)

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.8, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)
Pred = regressor.predict(features_test)
Score = regressor.score(features_train, labels_train)
Score = regressor.score(features_test, labels_test)
print("Score:",Score)


from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)


regressor = LinearRegression()
regressor.fit(features_poly, labels)





plt.scatter(features, labels, color = 'red')
plt.plot(features, regressor.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()

print("Predicting result with Polynomial Regression:")
x=[5]
x=np.array(x).reshape(1,-1)
print(regressor.predict(poly_object.transform(x)))




