import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


run = {
    "player" :["Kohli","Rohit","Warner"],
    "centuries" : [81,49,49],
    "Runs" : [30,10,26],
    "100s in 2018" : [54,32,22],
    "100s in 2019" : [9,9,8]
}

ff  = pd.DataFrame(run)

sns.kdeplot(data=ff,x="centuries",hue='player')
plt.show()