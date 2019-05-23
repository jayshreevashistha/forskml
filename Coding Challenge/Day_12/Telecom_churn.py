# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:05:21 2019

@author: computer
"""

import pandas as pd




df = pd.read_csv("Telecom_churn.csv")
churned_df = df[df['churn'] == True]
churned_count = df['churn'][(df['international plan']=='yes')& (df['voice mail plan']=='yes')].value_counts(normalize = True)
print("churned customer:",churned_count)
call_charge = df.groupby('churn')['total intl charge'].sum()
visual_1 = call_charge.plot.pie(autopct='%1.1f%%')

night_call = df['total night minutes'].max()
print(" highest night call minutes",night_call)
"""
call_analysis = df.iloc[:, 7:19].sum().sort_index()
visual_2 = call_analysis.plot.bar()
"""
non_churn_al = df['account length'][df['churn'] == False].max()
churn_al = churned_df['account length'].max()
if churn_al > non_churn_al:
    print('churned user have the maximum account lenght')
else:
    print('regular user have the maximum account lenght')


customer_care = churned_df['customer service calls'].value_counts()
print("customer_care:",customer_care)
area_pop = df.groupby('area code')['international plan'].value_counts().unstack()
print("area_pop:",area_pop)