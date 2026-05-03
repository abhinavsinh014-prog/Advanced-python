# arr = [1, 2, 3, 4, 5]

# reversed_arr = []
# for i in range(len(arr)-1, -1, -1):
#     reversed_arr.append(arr[i])

# print("Reversed list:", reversed_arr)

# arr = [1, 2, 3, 2, 4, 5, 1]

# duplicates = []
# for num in arr:
#     if arr.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print("Duplicates:", duplicates)

# # calculator.py
# # a = float(input("Enter first number: "))
# # b = float(input("Enter second number: "))

# # print("Addition:", a + b)
# # print("Subtraction:", a - b)
# # print("Multiplication:", a * b)

# # if b != 0:
# #     print("Division:", a / b)
# # else:
# #     print("Division by zero not allowed")

# # frequency_count.py
# arr = [1, 2, 2, 3, 3, 3, 4]

# freq = {}

# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# print("Frequency:", freq)

# num = int(input("Enter number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("It's not a Prime")
#             break
#     else:
#         print("It's a Prime Number")
# else:
#     print("It's not a Prime")


# rock_paper_scissors.py
# import random


# choices = ["rock", "paper", "scissors"]

# def get_user_choice():
#     return input("Enter rock/paper/scissors: ").lower()

# def get_computer_choice():
#     computer = random.choice(choices)
#     return computer

# def validate_user_choice(user, computer):
#     if user == computer:
#         return("Draw")
#     elif (user == "rock" and computer == "scissors") or \
#         (user == "paper" and computer == "rock") or \
#         (user == "scissors" and computer == "paper"):
#         return("You Win")
#     else:
#         return("You Lose")
    

# get1 = get_user_choice()
# get2 = get_computer_choice()    
# result = validate_user_choice(get1, get2)
# print(f"You chose: {get1}, Computer chose: {get2}. \nResult: {result}")   

