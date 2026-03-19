import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Name': ['ANSH', 'SAHIL', 'JAYAN', 'ANURAG'], 'Age': [21, 23, 20, 64]}
df = pd.DataFrame(data)

# sns.scatterplot(x=df.index,y='Age',data=df)
# sns.boxplot(y='Age', data=df)
# sns.violinplot(y='Age', data=df)
sns.swarmplot(x=df.index, y='Age', data=df,color = 'red')
plt.show()