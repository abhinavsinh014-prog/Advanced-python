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
first = data.loc["Avery Bradley"]
second = data.loc["Tyus Jones"]

print(first,"\n\n\n",second)