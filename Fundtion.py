def intro() -> str:
    return "Welcome to the Python programming world!"


msd = intro()
print(msd)
print(msd+' This is a simple function that returns a welcome message.')

def odd_even(list1):
    odd = []
    even = []
    for num in list1:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return odd, even
