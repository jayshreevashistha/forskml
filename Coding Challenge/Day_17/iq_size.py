# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:35:24 2019

@author: computer
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("iq_size.csv")
features = dataset.iloc[:, 1:4].values
labels = dataset.iloc[:, 0].values

import statsmodels.api as sm
features = sm.add_constant(features)


features_opt = features[:, [0,1,2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [ 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

x=[1,90,70,150]
x=np.array(x).reshape(1,-1)
print("IQ Level:",regressor.predict(x))




