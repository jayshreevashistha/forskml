# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:25:11 2019

@author: computer
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

dataset = pd.read_csv("PastHires.csv")  

#Preparing the dataset

features = dataset.iloc[:,:-1].values  
labels = dataset.iloc[:, 6].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,1] = labelencoder.fit_transform(features[:, 1])
features[:,3]= labelencoder.fit_transform(features[:,3])
features[:,4] = labelencoder.fit_transform(features[:,4])
features[:,5] = labelencoder.fit_transform(features[:,5])




from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20,random_state=0)   

#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 


#confusion matrix
from sklearn.metrics import confusion_matrix  
print("cm_df:",confusion_matrix(labels_test, labels_pred))  


Score = classifier.score(features_test,labels_test)
print("Score:",Score)



# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  



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


x=[10,1,4,0,1,0]
y=[10,0,4,1,0,1]
x=np.array(x).reshape(1,-1)
y=np.array(x).reshape(1,-1)
print("Hired: ",classifier.predict(x))
print("Hired: ",classifier.predict(y))