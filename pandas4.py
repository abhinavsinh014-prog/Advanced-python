from scipy import stats
import numpy as np
import pandas as pd

data = {'Age': [22, 25, 28, 24, 23, 29, 150, 27, 26, 22]}
df = pd.DataFrame(data)

z = np.abs(stats.zscore(df['Age']))
print("Z-Score Values:\n", z)

outliers = df[z > 3]
print("Outliers:\n", outliers)