from pathlib import Path
import json


# def greet_user():
#     path = Path("src/data/username.json")
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")


# greet_user()


# def get_stored_username():
#     path = Path("src/data/username.json")
#     if path.exists():
#         contents = path.read_text()
#         return json.loads(contents)
#     return None


# def greet_user():
#     path = Path("src/data/username.json")
#     username = get_stored_username()
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         path.write_text(json.dumps(username))
#         print(f"We'll remember you when you come back, {username}!")


# greet_user()


def get_stored_username():
    path = Path("src/data/username.json")
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    return None


def get_new_username(path):
    username = input("What is your name? ")
    path.write_text(json.dumps(username))
    return username


def greet_user():
    path = Path("src/data/username.json")
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
