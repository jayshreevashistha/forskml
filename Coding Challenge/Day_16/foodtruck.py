# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:54:19 2019

@author: computer
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

dataset = pd.read_csv('Foodtruck.csv')  

features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values.reshape(97,1)


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

print(regressor.intercept_)  
print (regressor.coef_)
x=[3.073]
x=np.array(x).reshape(1,-1)
#print (regressor.coef_*3.073 + regressor.intercept_)
print(regressor.predict(x))
"""

import pandas as pd
import matplotlib.pyplot as plt

#Importing 12.828
dataset = pd.read_csv("Foodtruck.csv")
#print dataset.describe()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#Splitting
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#   Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results,compare it with y_test
y_pred = regressor.predict(X_test)
print (y_pred)


# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Population vs Profit (Training set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'red')
plt.title('Population vs Profit (Training set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()
"""