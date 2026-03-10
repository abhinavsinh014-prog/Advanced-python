import pandas as pd

data = [7,5,6,4,3,2]         #Creating a Pandas Series

ser = pd.Series(data)
print(ser)

dat = ['A','U','R','A','F','A','R','M','E','R']
sen = pd.Series(dat)
print(sen[:4])