from pathlib import Path
import json

favorite_number = input("What is your favorite number? ")

path = Path("src/data/favorite_number.json")
contents = json.dumps(favorite_number)
path.write_text(contents)

contents = path.read_text()
favorite_number = json.loads(contents)

print(f"I know your favorite number! It's {favorite_number}.")