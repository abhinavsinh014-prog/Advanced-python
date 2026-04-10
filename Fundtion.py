# def intro() -> str:
#     return "Welcome to the Python programming world!"


# msd = intro()
# print(msd)
# print(msd+' This is a simple function that returns a welcome message.')

# def odd_even(list1):
#     odd = []
#     even = []
#     for num in list1:
#         if num % 2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)
#     return odd, even


# num1, num2 = odd_even([31,45,18,17,7,10,56,4,36,89,25,12,77,333])
# print("Odd numbers:", num1)
# print("Even numbers:", num2)

def van(name,wins):
    return f"{name} has won {wins} times championship."


nms = van("John cena",17)
print(nms)

def jain(*args,**kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

jain(1, 2, 3, name="Klaus", age=1000)

lst = list([1,2,3])
dict = dict(name="Klaus", age=1000)
