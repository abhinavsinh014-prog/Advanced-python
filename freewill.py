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
    "aditi" : {"balance":95454, "PIN":1234},
    "naman" : {"balance":89878, "PIN":5678},
    "randy" : {"balance":652525, "PIN":9012},
    "john"  : {"balance":31218, "PIN":3456},
    "pandat" : {"balance":31982, "PIN":7890},
    "gadariya":{"balance":56512, "PIN":2345},
    "mohit"  : {"balance":28879, "PIN":4567}
}
running = True
print("======= AURA FARMER BANK ATM =======")

while running :
    todo = input("Want to open new account or already have account (old/new/exit):-").lower().strip()
    
    def old_account():
        if todo == "old" :
            person = input("Enter your name:-").lower().strip()
            
            if person in bank:
                pin  = int(input("Enter your PIN :- "))

                if pin == bank[person]["pin"]:
                    print(f"Welcome {person.capitalize()}!")
                
                    while True:
                        action = input("Choose an action (check balance, deposit, withdraw, logout): ")
                        
                        if action == "check balance":
                            print(f"Your current balance is: ${bank[person]}")
                        
                        elif action == "deposit":
                            amount = float(input("Enter amount to deposit: "))
                            
                            if amount > 0:
                                bank[person]["balance"] += amount
                                print(f"${amount} deposited.\nNew balance is: ${bank[person]['balance']}")
                            
                            else:
                                return "Invalid deposit amount."
                        
                        elif action == "withdraw":
                            amount = float(input("Enter amount to withdraw: "))
                            
                            if 0 < amount <= bank[person]["balance"]:
                                bank[person]["balance"] -= amount
                                print(f"${amount} withdrawn.\nNew balance is: ${bank[person]['balance']}")
                            
                            else:
                                return "Invalid withdrawal amount or insufficient funds."
                        
                        elif action == "logout":
                            return "Exiting the ATM simulation. Goodbye!"
                            break
                        
                        else:
                            return "Invalid action. Please try again!"
                else:
                    return "Incorrect PIN. Access denied."
        else:
            return "Invalid action. Please try again!"
    def new_account():
        if todo == "new":
            ac_name = input("Enter your registered name :-").lower().strip()
            
            if ac_name in bank:
                print("account already registered")
            
            else:
                deposit_money = int(input("deposit money :-"))
                pin =int(input("set your 4 digit pin :-"))
                
                if deposit_money > 0:
                    bank[ac_name] = {"balance": deposit_money, "pin": pin}
                    return "succesfully registered !"
                
                else:
                    return "Invalid deposit amount."
        
    elif todo == "exit":
        print("Thanks for visitng")
        running = False
    
    else:
        print("invalid demand !!")