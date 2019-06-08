# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:07:33 2019

@author: computer
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('tree_addhealth.csv')

for i in dataset:
    dataset[i] = dataset[i].fillna(dataset[i].mode()[0])

features = dataset.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]].values
labels = dataset.iloc[:, 7].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)


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



"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split as TTS
from sklearn.metrics import confusion_matrix, accuracy_score


data = pd.read_csv("tree_addhealth.csv")

# Removing NaN values with Most Frequent value of the column
for i in data:
    data[i] = data[i].fillna(data[i].mode()[0])


######## Solution for Part 1 ########

# Separating Dependent and Independent variables as per Problem Statement
fe = data[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           'DEP1','ESTEEM1']].values
la = data["TREG1"].values

# Splitting the Data into Test and Train
ftr,fte,ltr,lte = TTS(fe,la,test_size=.2,random_state=0)

# Applying DecisionTreeClassifier
classi = DecisionTreeClassifier(criterion="entropy",random_state=0)
classi.fit(ftr,ltr)
pred = classi.predict(fte)

# Building Confusion Matrix
cm = confusion_matrix(pred,lte)

# Getting Accuracy Score of the Model
acc_model_part1 = accuracy_score(lte,pred)

print ("Accuracy Score of the Model part 1 : "+str(round(acc_model_part1*100,2))+"%")

######## Solution for Part 2 ########

# Separating Dependent and Independent variables as per Problem Statement
fe = data[["BIO_SEX","VIOL1"]].values
la = data["EXPEL1"].values

# Splitting the Data into Test and Train
ftr,fte,ltr,lte = TTS(fe,la,test_size=.2,random_state=0)

# Applying DecisionTreeClassifier
classi.fit(ftr,ltr)
pred = classi.predict(fte)

# Building Confusion Matrix
cm = confusion_matrix(pred,lte)

# Getting Accuracy Score of the Model
acc_model_part2 = accuracy_score(lte,pred)

print ("Accuracy Score of the Model part 2 : "+str(round(acc_model_part2*100,2))+"%")

######## Solution for Part 3 ########

# Separating Dependent and Independent variables as per Problem Statement
fe = data[['WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN']].values
la = data["TREG1"].values

ftr,fte,ltr,lte = TTS(fe,la,test_size=.2,random_state=0)

# Applying RandomForestClassifier
classi = RandomForestClassifier(n_estimators=10,criterion="entropy", 
                                random_state=0)
classi.fit(ftr,ltr)
pred = classi.predict(fte)

# Building Confusion Matrix
cm = confusion_matrix(pred,lte)

# Getting Accuracy Score of the Model
acc_model_part3 = accuracy_score(lte,pred)

print ("Accuracy Score of the Model part 3 : "+str(round(acc_model_part3*100,2))+"%")
"""
