import pandas as pd
import numpy as np
import seaborn as sns

sns.get_dataset_names()

penguins = sns.load_dataset("penguins")
penguins.head()
print(penguins)
 
penguins["species"].value_counts()
# print(penguins["island"].value_counts())