from pathlib import Path
import json


def get_stored_user_info(path):
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    return None


def get_new_user_info(path):
    username = input("What is your name? ")
    favorite_number = input("What is your favorite number? ")
    favorite_color = input("What is your favorite color? ")

    user_info = {
        "username": username,
        "favorite_number": favorite_number,
        "favorite_color": favorite_color,
    }

    path.write_text(json.dumps(user_info))
    return user_info


def greet_user():
    path = Path("src/data/user_info.json")
    username = get_stored_user_info(path)
    if username:
        correct = input(f"Are you {username['username']}? (yes/no) ")
        if correct == 'yes':
            print(f"Welcome back, {username['username']}!")
        else:
            user_info = get_new_user_info(path)
            print(f"We'll remember you when you come back, {
                  user_info['username']}!")
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {
              user_info['username']}!")


greet_user()
