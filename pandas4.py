import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Age': [22, 25, 28, 24, 23, 29, 150, 27, 26, 22]}
df = pd.DataFrame(data)

sns.boxplot(x=df['Age'])
plt.title("Box Plot for Age")
plt.show()