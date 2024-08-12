from pathlib import Path
import json

path = Path('src/data/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
