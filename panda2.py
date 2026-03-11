import pandas as pd

# data = [7,5,6,4,3,2]         #Creating a Pandas Series

# ser = pd.Series(data)
# print(ser)

# dat = ['A','U','R','A','F','A','R','M','E','R']    #Position-based Indexing
# sen = pd.Series(dat)
# print(sen[:4])

# datm = ['A','U','R','A','F','A','R','M','E','R']    #labled-based Indexing
# send = pd.Series(datm,index=[30,31,32,33,34,35,36,37,38,39])
# print(send[34])

df = pd.read_csv("wwe.csv")

serr = pd.Series(df['Name'])
data = serr.head(12)
print(data)

print(data.loc[0:3])