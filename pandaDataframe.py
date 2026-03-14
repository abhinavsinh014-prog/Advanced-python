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

# data = pd.read_csv("nba.csv",index_col="Name")
# first = data.loc["Avery Bradley"]   #row selection using iloc
# second = data.loc["Tyus Jones"]

# third = data["Age"]                #indexing operator

# fourth = data.iloc[0]              #row selection using loc

# print(first,"\n\n\n",second)

# print(fourth)

 
# import numpy as np
 
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score':[np.nan, 40, 80, 98]}

# df = pd.DataFrame(dict)
 
# print(df.isnull())
# print()

# print(df.notnull())
# print()

# print(df.fillna(0)) #any value you put here instead of 0 is replaced by that number in place of missing data 
# print(df.fillna(method='pad')) #it puts the previous value
# df.fillna(method='bfill')#it fills with backward value



# dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
#         'score':[90, 40, 80, 98]}
 
# df = pd.DataFrame(dict)

# for i, j in df.iterrows():               #Iterating Over Rows
#     print(i, j)
#     print()

# d = pd.read_csv("employees.csv")

# nmg = pd.notnull(d["Gender"])
# ngmd = d[nmg]

# print(ngmd)

# boll_series = pd.isnull(d["Gender"])
# missing_series= d[boll_series]
# print(missing_series)

# import numpy as np

# data = {'Name': ['Amit', 'Sita', np.nan, 'Raj'],
#         'Age': [25, np.nan, 22, 28]}

# df = pd.DataFrame(data)

# # Check for missing values using isna()
# print(df.isna())


# data = {
#     'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David'],
#     'Age': [25, 30, 25, 35, 30, 40],
#     'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'San Francisco']
# }

# df = pd.DataFrame(data)
# print(df)

# duplicates = df.duplicated()         # Using duplicated() Method
# print(duplicates)

# df_no_duplicates = df.drop_duplicates(subset = ["Name","City"])
# print(df_no_duplicates)

# df_keep_last = df.drop_duplicates(keep='last')
# (df_keep_last)


data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']}
df = pd.DataFrame(data1)
print(df)


df.groupby('Name')
print(df.groupby('Name').groups)

gk = df.groupby('Name') 
print(gk.first())

df.groupby(['Name', 'Qualification'])
print(df.groupby(['Name', 'Qualification']).groups)

print(df.groupby('Name')['Age'].sum())

print(df.groupby(['Name'], sort=False)['Age'].sum())

grp = df.groupby('Name')
for name, group in grp:
    print(name)
    print(group)
    print()