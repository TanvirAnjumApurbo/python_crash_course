from pathlib import Path

path = Path('src\data\guest.txt')
name = input("What is your name? ")
path.write_text(name)
