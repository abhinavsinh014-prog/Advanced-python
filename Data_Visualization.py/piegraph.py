import matplotlib.pyplot as plt
import pandas as pd

stars = ['john cena','randy orton','triple h','edge','the rock']
wins = [1700,1254,1104,1100,1998]

plt.pie(wins,labels=stars, autopct= "%1.2f", explode = [0, 0.1, 0.2,0.1,0.1])
plt.title("wins")
plt.show()