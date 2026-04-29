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

# calculator.py
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)

# if b != 0:
#     print("Division:", a / b)
# else:
#     print("Division by zero not allowed")

# frequency_count.py
arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency:", freq)