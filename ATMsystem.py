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

command = input("Want to open new account or already have account (old/new/exit): ").lower().strip()


def old_account():
    person = input("Enter your name: ").lower().strip()

    if person in bank:
        pin = int(input("Enter your PIN: "))

        if pin == bank[person]["pin"]:
            print(f"Welcome {person.capitalize()}!")

            while True:
                action = input("Choose action (check balance, deposit, withdraw, logout): ").lower().strip()

                if action == "check balance" or action == "balance":
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
            print("Successfully registered!!")
            print(f"Your new balance is: ₹{bank[ac_name]['balance']}")
        else:
            print("Invalid deposit amount.")


