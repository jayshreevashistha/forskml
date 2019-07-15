# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:58:10 2019

@author: computer
"""

import pandas as pd
import numpy as np

with open('Advertisement_training_data.json') as f:
    data1 = f.read()
    
with open('Advertisement_test_data.json',encoding="utf-8") as f:
    data2 = f.read()

data1 = data1[data1.find("{"):]
data2 = data2[data2.find("{"):]
training = pd.read_json(data1,lines=True)
test = pd.read_json(data2,lines=True)

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
corpus = []


for i in range(0, 20217):
    head = re.sub('[^a-zA-Z]', ' ', training['heading'][i])
    head = head.lower()
    head= head.split()
    head = [word for word in head if not word in set(stopwords.words('english'))]
    
    ps = PorterStemmer()
    head = [ps.stem(word) for word in head]
    head = ' '.join(head)
    corpus.append(head)
    

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = training.iloc[:, 0].values

features = np.append(features,training.loc[:,['city','section']].values,axis=1)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, -1] = labelencoder.fit_transform(features[:, -1])
features[:, -2] = labelencoder.fit_transform(features[:, -2])




#one hot encoding
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [1500,1501])
features = onehotencoder.fit_transform(features).toarray()

# dropping first column
features = features[:, 1:]