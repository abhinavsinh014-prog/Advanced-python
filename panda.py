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