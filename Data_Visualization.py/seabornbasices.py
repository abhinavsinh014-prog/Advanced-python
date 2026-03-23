import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.get_dataset_names()

penguins = sns.load_dataset("penguins")
penguins.head()
print(penguins)
 
print(penguins["species"].value_counts())
print(penguins["island"].value_counts())

# sns.set_style("ticks")
# sns.set_context("paper")
# sns.scatterplot(data=penguins,x="flipper_length_mm",y="body_mass_g",hue = "island",palette = "Set1")
# sns.despine(left = True)
# plt.show()

# sns.scatterplot(data=penguins,x="species",y="body_mass_g",hue = "island",style = 'sex',palette = "Set1",alpha = 0.5)
# plt.show()

# sns.stripplot(data=penguins,x="species",y="body_mass_g",hue = "island",dodge=True,jitter=True)
# plt.show()

# sns.swarmplot(data=penguins,x="species",y="body_mass_g",hue = "island")
# sns.despine()
# plt.show()

sns.histplot(data=penguins,x="body_mass_g",hue = 'sex',multiple = "stack")
plt.show()