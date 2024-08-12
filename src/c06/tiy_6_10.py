favorite_numbers = {
    'jen': [5, 7],
    'sarah': [7, 9],
    'edward': [9, 11],
    'phil': [3, 5],
    'jim': [8, 10],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
