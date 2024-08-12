favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

list_of_people = ['jen', 'sarah', 'edward', 'phil', 'erin', 'joe', 'jane']

for person in list_of_people:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll.")
