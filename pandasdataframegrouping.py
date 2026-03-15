import pandas as pd
import numpy as np

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
# for name, group in grp:
#     print(name)
#     print(group)
#     print()

print(grp.get_group('Jai'))

grp = df.groupby(['Name','Qualification'])

print(grp.get_group(('Jai','Msc')))

grp1 = df.groupby('Name')
print(grp1['Age'].aggregate(np.sum))


grp2 = df.groupby(['Name','Qualification'])
print(grp2['Age'].aggregate(np.sum))

grp3 = df.groupby('Name')
print(grp3['Age'].agg([np.sum, np.mean, np.std]))
