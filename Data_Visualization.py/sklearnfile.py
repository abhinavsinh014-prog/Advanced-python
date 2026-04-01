from sklearn.datasets import fetch_california_housing

X ,y = fetch_california_housing(return_X_y=True)

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
mod = LinearRegression()

mod.fit(X,y)

pred = mod.predict(X)

plt.scatter(pred,y)