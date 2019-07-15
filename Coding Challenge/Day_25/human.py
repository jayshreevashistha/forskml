# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:45:40 2019

@author: computer
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
df_1 = pd.read_csv('test.csv')
features_test = df_1.iloc[:, :-1].values
labels_test = df_1.iloc[:, 562].values

df_2 = pd.read_csv('train.csv')
features_train = df_2.iloc[:, :-1].values
labels_train = df_2.iloc[:, 562].values



#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 


#confusion matrix
from sklearn.metrics import confusion_matrix  
print("cm_df:",confusion_matrix(labels_test, labels_pred))  


Score_dt = classifier.score(features_test,labels_test)
print("Score_dt:",Score_dt)



from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print("cm_rf:",confusion_matrix(labels_test,labels_pred))  
print("cr:",classification_report(labels_test,labels_pred))  
print("AS:",accuracy_score(labels_test, labels_pred))
Score_rf = classifier.score(features_test,labels_test)
print("Score_rf:",Score_rf)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
Score_lr = classifier.score(features_test,labels_test)
print("Score_lr:",Score_lr)


# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)
Score_knn = classifier.score(features_test,labels_test)
print("Score_knn:",Score_knn)


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels_train = labelencoder.fit_transform(labels_train)
# Building the optimal model using Backward Elimination
import statsmodels.api as sm



features_opt = features_train
regressor_OLS = sm.OLS(endog = labels_train, exog = features_opt).fit()
regressor_OLS.summary()

y = pd.DataFrame(labels_train)
x =pd.DataFrame(features_train)
cols = list(x.columns)
pmax=1
while(len(cols)>0):
    p=[]
    x_1 = x[cols]
    x_1 = sm.add_constant(x_1)
    model = sm.OLS(y,x_1).fit()
    p = pd.Series(model.pvalues.values[1:],index=cols)
    pmax=max(p)
    feature_with_p_max = p.idxmax()
    if(pmax>0.05):
        cols.remove(feature_with_p_max)
    else:
        break
selected_features_BE = cols
print(selected_features_BE)

features_train1 = features_train[:,selected_features_BE] 
labels_train1 = labels_train

features_test1 = features_test[:,selected_features_BE]
labels_test1 = labels_test


