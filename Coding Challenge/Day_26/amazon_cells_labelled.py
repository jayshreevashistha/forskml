# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:15:16 2019

@author: computer
"""

import pandas as pd

dataset = pd.read_csv('amazon_cells_labelled.txt',names=["Review", "liked"],delimiter = '\t')

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
corpus = []


for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:, 1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)


Score_knn = classifier.score(features_test,labels_test)
print("Score_knn:",Score_knn)


from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm_svm = confusion_matrix(labels_test, labels_pred)

Score_svm = classifier.score(features_test,labels_test)
print("Score_svm:",Score_svm)


from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
gnb = GaussianNB()


# Train classifier
gnb.fit(features_train, labels_train)
labels_pred = gnb.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_gnb = confusion_matrix(labels_test, labels_pred)

Score_nb = classifier.score(features_test,labels_test)
print("Score_nb:",Score_nb)