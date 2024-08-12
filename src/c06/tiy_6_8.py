pet_1 = {
    'name': 'dog',
    'owner': 'john',
    'color': 'brown',
}

pet_2 = {
    'name': 'cat',
    'owner': 'jane',
    'color': 'black',
}

pet_3 = {
    'name': 'fish',
    'owner': 'joe',
    'color': 'gold',
}

pet_4 = {
    'name': 'rooster',
    'owner': 'tanvir',
    'color': 'white',
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['color']} {pet['name']}.")
