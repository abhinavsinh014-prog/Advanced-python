import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = [12,11,14,17,16]
y = [50,55,62,63,45]

plt.plot(x,y)
plt.title("line chart")
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.show()

x = ['john cena','randy orton','triple h','edge','the rock']
y = [17,14,14,11,10]

plt.bar(x,y)
plt.title("world title")
plt.xlabel("superstars")
plt.ylabel("championship")
plt.show()

x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
     21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]

plt.hist(x, bins=10, color='steelblue')
plt.title("Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

x = ['john cena','randy orton','triple h','edge','the rock']
y = [1700,1254,1104,1100,1998]

plt.scatter(x,y)
plt.title("world title")
plt.xlabel("superstars")
plt.ylabel("wins")
plt.show()

stars = ['john cena','randy orton','triple h','edge','the rock']
wins = [1700,1254,1104,1100,1998]

plt.pie(wins,labels=stars)
plt.title("wins")
plt.show()