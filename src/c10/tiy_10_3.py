from pathlib import Path

path = Path('src\data\learning_python.txt')
contents = path.read_text()
print(contents)

print("")

for line in contents.splitlines():
    print(line)
