class User:
    def __init__(self, first_name, last_name, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"Their username is {self.username}.")

    def greet_user(self):
        print(f"Hello, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


user_1 = User('John', 'Doe', 30, 'johndoe')

print(f"Login attempts: {user_1.login_attempts}")
print(f"Login attempts: {user_1.increment_login_attempts()}")
print(f"Login attempts: {user_1.increment_login_attempts()}")
print(f"Login attempts: {user_1.increment_login_attempts()}")
print(f"Login attempts: {user_1.increment_login_attempts()}")
print(f"Login attempts: {user_1.increment_login_attempts()}")
print(f"Login attempts: {user_1.reset_login_attempts()}")




