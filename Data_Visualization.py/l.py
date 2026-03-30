import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


run = {
    "player" :["Kohli","Rohit","Warner","Smith","Root"],
    "centuries" : [81,49,49,44,59],
    "Runs" : [30,10,26,38,41],
    "100s in 2018" : [54,32,22,12,18],
    "100s in 2019" : [9,9,8,6,4]
}

ff  = pd.DataFrame(run)

sns.kdeplot(data=ff,x="centuries",color='red')
plt.show()

