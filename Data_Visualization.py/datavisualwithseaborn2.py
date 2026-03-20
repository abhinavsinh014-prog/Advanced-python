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

#How to Customize Seaborn Plots with Python?

#Adding Titles and Axis Labels

iris = sns.load_dataset('iris')
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)

plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()