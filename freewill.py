arr = [1, 2, 3, 4, 5]

reversed_arr = []
for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])

print("Reversed list:", reversed_arr)

arr = [1, 2, 3, 2, 4, 5, 1]

duplicates = []
for num in arr:
    if arr.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicates:", duplicates)