add = {"apple": 1, "banana": 2, "orange": 3, "grape": 4, "melon": 5}
def add_fruits(fruit_dict):
    total = 0
    for fruit, quantity in fruit_dict.items():
        total += quantity
    return total