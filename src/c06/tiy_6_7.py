person_1 = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 30,
    'city': 'new york',
}

person_2 = {
    'first_name': 'jane',
    'last_name': 'smith',
    'age': 25,
    'city': 'los angeles',
}

person_3 = {
    'first_name': 'joe',
    'last_name': 'brown',
    'age': 35,
    'city': 'chicago',
}

people = [person_1, person_2, person_3]

for person in people:
    print(person['first_name'].title())
    print(person['last_name'].title())
    print(person['age'])
    print(person['city'].title())
    print("\n")
