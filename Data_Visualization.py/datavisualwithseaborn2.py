from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# iris = load_iris()
# df = pd.DataFrame(iris.data, columns=iris.feature_names)
# df['Species'] = iris.target
# df['Species'] = df['Species'].map({ 0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

# sns.kdeplot(data=df[df['Species'] == 'Virginica'], x='sepal length (cm)', fill=True, label='Virginica')
# plt.legend()
# plt.show()

##How to Customize Seaborn Plots with Python?

#Adding Titles and Axis Labels

iris = sns.load_dataset('iris')
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris,color='yellow')

plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

##Built-in Styles and Grids in Seaborn

# sns.set_style("whitegrid")

# sns.boxplot(x='species', y='petal_length', data=sns.load_dataset('iris'),color = 'red')
# plt.title('Petal Length Distribution by Species')
# plt.show()

##Customizing Color Palettes

# sns.set_palette("pastel") 

# sns.violinplot(x='species', y='petal_length', data=sns.load_dataset('iris'),color ='green')
# plt.title('Petal Length Distribution by Species')
# plt.show()

##Using custom plate
# custom_colors = ['#FF5733', '#33FFBD', '#335BFF']
# sns.set_palette(custom_colors)

# sns.violinplot(x='species', y='petal_length', data=sns.load_dataset('iris'))
# plt.title('Custom Colored Petal Length Distribution')
# plt.show()

##Adjusting Figure Size and Aspect Ratio
# plt.figure(figsize=(10, 6))

# sns.lineplot(x='year', y='passengers', data=sns.load_dataset('flights'),marker = 'o',color = 'green')
# plt.title('Number of Passengers Over Time')
# plt.show()


