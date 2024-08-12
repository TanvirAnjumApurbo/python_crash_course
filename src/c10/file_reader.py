from pathlib import Path

path = Path('src\data\pi_digits.txt')
contents = path.read_text()
print(contents)

contents = path.read_text().rstrip()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)
