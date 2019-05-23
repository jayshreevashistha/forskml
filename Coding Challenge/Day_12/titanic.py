# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:56:03 2019

@author: computer
"""
import pandas as pd

df = pd.read_csv("training_titanic.csv")
df_survive=pd.DataFrame(df['Survived'].value_counts())


survive=df['Survived'].value_counts(normalize = True)[1]
print ("Survived : "+str(round(survive*100, 2))+"%")
died = df['Survived'].value_counts(normalize = True)[0]
print ("Died : "+str(round(died*100, 2))+"%")


male_survive= df['Survived'][df['Sex'] == 'male'].value_counts(normalize=True)[1]
male_died= df['Survived'][df['Sex'] == 'male'].value_counts(normalize=True)[0]
print ("male_survived : "+str(round(male_survive*100,2))+"%")
print ("male_died : "+str(round(male_died*100,2))+"%")
female_survive= df['Survived'][df['Sex'] == 'female'].value_counts(normalize=True)[1]
female_died = df['Survived'][df['Sex'] == 'female'].value_counts(normalize=True)[0]
print ("female_survived : "+str(round(female_survive*100,2))+"%")
print ("female_died : "+str(round(female_died*100,2))+"%")


Child=df["Child"] = df["Age"].map(lambda x: 1 if x <18 else 0 )

child_survive=df['Survived'][df['Child']==1].value_counts(normalize = True)[1]
print ("Child Survived : "+str(round(child_survive*100, 2))+"%")


adult_survive=df['Survived'][df['Child']==0].value_counts(normalize = True)[1]
print ("Adult Survived : "+str(round(adult_survive*100, 2))+"%")

   
"""
import pandas as pd

data = pd.read_csv('training_titanic.csv')

data.shape

data.info()

data.head(10)

data['Survived'].value_counts()


disaster_survived = data['Survived'].value_counts()[1]

disaster_died = data['Survived'].value_counts()[0]

disaster_survived_percentage = data['Survived'].value_counts(normalize=True)[1]

disaster_died_percentage = data['Survived'].value_counts(normalize=True)[0]

male_survived = data['Survived'][data['Sex'] == 'male'].value_counts(normalize=True)[1]
male_passed_away =  data['Survived'][data['Sex'] == 'male'].value_counts(normalize=True)[0]

female_survived = data['Survived'][data['Sex'] == 'female'].value_counts(normalize=True)[1]
female_passed_away =  data['Survived'][data['Sex'] == 'female'].value_counts(normalize=True)[0]


print ("disaster_survived : "+str(disaster_survived))
print ("disaster_died : "+str(disaster_died))
print ("disaster_survived_percentage : "+str(round(disaster_survived_percentage*100,2))+"%")
print ("disaster_died_percentage : "+str(round(disaster_died_percentage*100,2))+"%")
print ("male_survived : "+str(round(male_survived*100,2))+"%")
print ("male_passed_away : "+str(round(male_passed_away*100,2))+"%")
print ("female_survived : "+str(round(female_survived*100,2))+"%")
print ("female_passed_away : "+str(round(female_passed_away*100,2))+"%")


data['Child'] = 0
data['Child'][data['Age'] < 18] = 1
c =  data['Survived'][data['Child'] == 1].value_counts(normalize=True)
print ("Child Survived : "+str(round(c[1]*100, 2))+"%")




"""