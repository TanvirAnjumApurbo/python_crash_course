from pathlib import Path

path = Path('src\data\learning_python.txt')
contents = path.read_text()
print(contents)

print("")

lines = contents.splitlines()
for line in lines:
    print(line)
