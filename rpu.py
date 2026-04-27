quantity = {"apple": 1, "banana": 2, "orange": 3, "grape": 4, "melon": 5}
price = {"apple": 1.5, "banana": 0.5, "orange": 0.75, "grape": 2.0, "melon": 3.0}
def add_fruits(fruit_dict):
    total = 0
    for fruit, quantity in fruit_dict.items():
        total += quantity
    return total

def calculate_total_cost(fruit_dict, price_dict):
    total = 0
    for fruit, quantity in fruit_dict.items():
        total += quantity * price_dict.get(fruit, 0)
    return total

if __name__ == "__main__":
    total_fruits = add_fruits(quantity)
    print(f"Total fruits: {total_fruits}")
    total_cost = calculate_total_cost(quantity, price)
    print(f"Total cost: ${total_cost:.2f}")
    
