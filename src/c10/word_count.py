from pathlib import Path


def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


file_names = ['alice.txt', 'siddhartha.txt',
              'romeo_juliet.txt', 'the_whale.txt']

for file_name in file_names:
    path = Path(f'src/data/{file_name}')
    count_words(path)
