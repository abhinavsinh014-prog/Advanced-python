import pandas as pd


run = {
    "player" :["Kohli","Rohit","Warner","Smith","Root"],
    "100s in 2016" : [7,5,7,4,4],
    "100s in 2017" : [11,7,5,6,4],
    "100s in 2018" : [11,8,0,0,5],
    "100s in 2019" : [7,10,7,4,4]
}

ff  = pd.DataFrame(run)

print(ff)