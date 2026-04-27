add = {"apple": 1, "banana": 2, "orange": 3, "grape": 4, "melon": 5}
def add_fruits(fruit_dict):
    total = 0
    for fruit, quantity in fruit_dict.items():
        total += quantity
    return total

if __name__ == "__main__":
    total_fruits = add_fruits(add)
    print(f"Total fruits: {total_fruits}")