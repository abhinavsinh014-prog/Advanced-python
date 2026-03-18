import matplotlib.pyplot as plt
import pandas as pd
marks = {
    "marks":[36,48,56,78,98,56,45,25,65,45,85,74,96,36,36,96,52]
}

fg = pd.DataFrame(marks)

plt.plot(fg['marks'],color='red',marker='p',linestyle='-',linewidth = '2')
plt.title("line chart")
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.grid()
plt.show()