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

# sns.histplot(data=penguins,x="body_mass_g",hue = 'sex',multiple = "stack")
# plt.show()

# sns.regplot(data=penguins,x="body_mass_g",y='flipper_length_mm',color='red',scatter=False)
# plt.show()

# sns.lineplot(data=penguins,x="body_mass_g",y='flipper_length_mm',color='red',hue='island',style='sex')
# plt.show()

# sns.jointplot(data=penguins,x="body_mass_g",y='flipper_length_mm',hue='sex',kind='scatter')
# plt.show()

# sns.barplot(data=penguins,x="species",y='body_mass_g',hue='sex',palette=['pink','blue'],estimator=np.sum)
# plt.show()

# sns.countplot(data=penguins,x="species",hue='island',palette='Set1')
# plt.show()

# sns.boxplot(data=penguins,x="species",y="body_mass_g",hue='sex',palette='Set1')
# plt.show()

# sns.violinplot(data=penguins,x="species",y="body_mass_g",hue='sex',split = True)
# plt.show()

sns.kdeplot(data=penguins,x="body_mass_g",hue="species",palette="pastel",fill =True)
plt.show()