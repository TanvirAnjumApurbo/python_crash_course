from pathlib import Path

path = Path('src/data/middlemarch.txt')
contents = path.read_text(encoding='utf-8')

# This will count 'then' and 'there' too.
the_count_1 = contents.lower().count('the')
the_count_2 = contents.lower().count('the ')

print(f"The word 'the' appears {the_count_1} times in {path}.")
print(f"The word 'the ' appears {the_count_2} times in {path}.")
