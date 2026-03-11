import pandas as pd

lst = ['John cena','randy orton','triple h','edge','the rock']

lf = pd.DataFrame(lst)                 #creating pandas dataframe
print(lf)

 
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
 
df = pd.DataFrame(data)
 
print(df)