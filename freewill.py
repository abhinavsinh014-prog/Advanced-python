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

bank = {
    "aditi": {"balance": 95454, "pin": 1234},
    "naman": {"balance": 89878, "pin": 5678},
    "randy": {"balance": 65255, "pin": 9012},
    "john": {"balance": 31218, "pin": 3456},
    "pandat": {"balance": 31982, "pin": 7890},
    "gadariya": {"balance": 56512, "pin": 2345},
    "mohit": {"balance": 28879, "pin": 4567}
}

print("====== AURA FARMER BANK ATM ======")

todo = input("Want to open new account or already have account (old/new/exit): ").lower().strip()


def old_account():
    person = input("Enter your name: ").lower().strip()

    if person in bank:
        pin = int(input("Enter your PIN: "))

        if pin == bank[person]["pin"]:
            print(f"Welcome {person.capitalize()}!")

            while True:
                action = input("Choose action (check balance, deposit, withdraw, logout): ").lower().strip()

                if action == "check balance":
                    print(f"Your current balance is: ₹{bank[person]['balance']}")

                elif action == "deposit":
                    amount = int(input("Enter amount to deposit: "))

                    if amount > 0:
                        bank[person]["balance"] += amount
                        print(f"₹{amount} deposited. New balance: ₹{bank[person]['balance']}")
                    else:
                        print("Invalid deposit amount.")

                elif action == "withdraw":
                    amount = int(input("Enter amount to withdraw: "))

                    if 0 < amount <= bank[person]["balance"]:
                        bank[person]["balance"] -= amount
                        print(f"₹{amount} withdrawn. New balance: ₹{bank[person]['balance']}")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")

                elif action == "logout":
                    print("Exiting the ATM simulation. Goodbye!")
                    break

                else:
                    print("Invalid action. Please try again.")

        else:
            print("Incorrect PIN. Access denied.")
    else:
        print("Account not found.")


def new_account():
    ac_name = input("Enter your registered name: ").lower().strip()

    if ac_name in bank:
        print("Account already registered.")
    else:
        deposit_money = int(input("Deposit money: "))
        pin = int(input("Set your 4 digit PIN: "))

        if deposit_money > 0:
            bank[ac_name] = {"balance": deposit_money, "pin": pin}
            print("Successfully registered!")
            print(f"Your new balance is: ₹{bank[ac_name]['balance']}")
        else:
            print("Invalid deposit amount.")


def exit_account():
    print("Thanks for visiting!")


if todo == "old":
    old_account()

elif todo == "new":
    new_account()

elif todo == "exit":
    exit_account()

else:
    print("Invalid demand!")