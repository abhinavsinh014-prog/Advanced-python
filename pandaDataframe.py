import pandas as pd

# lst = ['John cena','randy orton','triple h','edge','the rock']

# lf = pd.DataFrame(lst)                 #creating pandas dataframe
# print(lf)

 
# data = {'Name':['Tom', 'nick', 'krish', 'jack'],          
#         'Age':[20, 21, 19, 18]}                #creating pandas dataframe by using dictionary
 
# df = pd.DataFrame(data)
 
# print(df)

# print()

# deta = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# gf = pd.DataFrame(deta)               #Column selection
 
# print(gf[['Name', 'Qualification']])

data = pd.read_csv("nba.csv",index_col="Name")
first = data.loc["Avery Bradley"]   #row selection using iloc
second = data.loc["Tyus Jones"]

third = data["Age"]                #indexing operator

fourth = data.iloc[0]              #row selection using loc

print(first,"\n\n\n",second)

print(fourth)

 
import numpy as np
 
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}

df = pd.DataFrame(dict)
 
print(df.isnull())
print()

print(df.notnull())
print()

print(df.fillna(25))