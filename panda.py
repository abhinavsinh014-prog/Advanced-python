import pandas as pd
import numpy as np

#Pandas Series
data = np.array(["A",'u','r','a'])

s = pd.Series(data)
print(s)

#Pandas DataFrame
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']

s = pd.DataFrame(lst)
print(s)

#Loading Data

p = pd.read_csv("p.csv")
print(p.head())

#info

print(p.info())

#Handling missing data

print(p.isnull().sum())
p = p.fillna(0)

#Selecting and Filtering Data
ages = p[(p['age']>25) & (p['sales']>220)] 
print(ages)

#Adding column
p['total'] = p['a'] + p['b']
print(p.head())

#Removing column
p=p.drop('city',axis =1 )
print(p.head())

#Grouping data
res = p.groupby('category')['sales'].sum()
print(res)