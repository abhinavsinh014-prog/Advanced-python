import matplotlib.pyplot as plt
import pandas as pd
 
x = ['john cena','randy orton','triple h','edge','the rock']
y = [17,14,14,11,10]

plt.bar(x,y,color = ["green", "black", "red","yellow","blue"])
plt.title("world title")
plt.xlabel("superstars")
plt.ylabel("championship")
plt.show()
