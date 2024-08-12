from pathlib import Path

filenames = ['cats.txt', 'dogs.txt', 'elephants.txt']

# for filename in filenames:
#     path = Path(f'src/data/{filename}')
#     contents = path.read_text()
#     for line in contents.splitlines():
#         print(line)

for filename in filenames:
    path = Path(f'src/data/{filename}')
    try:
        contents = path.read_text().title()
    except FileNotFoundError:
        pass
    else:
        for line in contents.splitlines():
            print(line)
