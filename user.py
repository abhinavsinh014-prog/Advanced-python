data = {
    "John cena": 1765,
    "The rock": 2810,
    "Iron man": 3980,
    "Captain America": 2155
}
input_name = input("Enter the name of the wrestler: ")
if input_name in data:
    print(f"{input_name} has a user code of {data[input_name]}.")
else:    print(f"{input_name} is not in the data.")