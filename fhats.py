a = [[5,6,9],[2,3,6]]
m = [ [4,5,6],[2,3,7]]

dd = [[a[i][j] + m[i][j] for j in range(len(a[0]))] for i in range(len(a))]
print("Aura addition:\n",dd)

b = 45
n = "45"
print(b+45)