# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 13:41:20 2022

@author: LUGAPEDE
"""

"""
data nalysis from udemy
"""
# import all the neccesary datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/LUGAPEDE/Documents/data_projects/Python_scripts/projects/salaries_by_college_major.csv')
df.head()
df.dtypes
df.columns
df.shape

# look for any missing value in the set
df.apply(lambda x: sum(x. isnull()))

df.tail()

df.dropna(inplace = True)


df.columns

# what major has the highest earnings
values = df.groupby(['Undergraduate Major'])['Mid-Career Median Salary'].mean()
values = pd.DataFrame(values)
values.sort_values(ascending = False)
type(values)

# or we can use max() and aidmax() on the same
df['Starting Median Salary'].idxmax()
df['Undergraduate Major'].iloc[43]

#low risk Majors
risk = df['Mid-Career 90th Percentile Salary'].subtract(df['Mid-Career 10th Percentile Salary'])
df.insert(1,'Spread', risk)
df.head()

low_risk = df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()


highest = df.sort_values('Mid-Career 90th Percentile Salary', ascending= False)
highest[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']]
    