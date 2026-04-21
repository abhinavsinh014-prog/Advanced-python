import pandas as pd

data = [7,5,6,4,3,2]         #Creating a Pandas Series

ser = pd.Series(data)
print(ser)

dat = ['A','U','R','A','F','A','R','M','E','R']    #Position-based Indexing
sen = pd.Series(dat)
print(sen[:4])

datm = ['A','U','R','A','F','A','R','M','E','R']    #labled-based Indexing
send = pd.Series(datm,index=[30,31,32,33,34,35,36,37,38,39])
print(send[34])

df = pd.read_csv("wwe.csv")

serr = pd.Series(df['Name'])                         
data = serr.head(12)
print(data)

print(data.loc[0:3])                             #Indexing a Series using .loc[]
print(data.iloc[0:4])                            #Indexing a Series using .iloc[]


#Binary Operations on Pandas Series

df1 = pd.Series([1,2,3],index=['A','B','C'])
df2 = pd.Series([4,5,66],index=['A','B','C'])

df_sum = df1.add(df2)
print(df_sum)                            #sum
print()

df_sub = df2.sub(df1)
print(df_sub)                            #substract
print()

df_mult = df2.mul(df1)
print(df_mult)                           #multiplication
print()

df_div = df2.div(df1)
print(df_div)                            #division
print()

de = pd.Series([1,3,5,7,8,19622])
de = de.astype(float)
print(de)