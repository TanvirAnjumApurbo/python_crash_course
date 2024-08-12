from pathlib import Path

path = Path('src\data\learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    contents = line.replace('Python', 'C')
    print(contents)
