from pathlib import Path

path = Path('src\data\guest_book.txt')

guest_list = ''
while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    else:
        guest_list += name+'\n'
        path.write_text(guest_list)
