n = int(input())
m = int(input())

grid = []
for i in range(n):
    ele = input().split()
    for j in range(m):
        ele[j] = int(ele[j])
    grid.append(ele)
print(grid) 

#short method
n = int(input()) 
grid = []
for i in range(n):
    grid.append([int(ele) for ele in input().split()])
print(grid)