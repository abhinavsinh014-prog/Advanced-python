data = {
    "Name": ["Naman", "Riya", "Karan", "Neha", "Vikram", "Priya", "Rahul", "Simran"],
    "Age": [20, 21, 19, 22, 20, 23, 21, 19],
    "City": ["Delhi", "Mumbai", "Ghaziabad", "Delhi", "Noida", "Mumbai", "Ghaziabad", "Noida"],
    "Marks": [85, 78, 92, 88, 67, 95, 73, 80],
    "Attendance": [90, 85, 95, 88, 70, 96, 75, 82]
}

import pandas as pd
df = pd.DataFrame(data)

df["Marks"].mean()

df[(df["Marks"] > 88) & (df["Attendance"] > 90)]
print(df)
df["Result"] = df["Marks"] > 75
print(df)