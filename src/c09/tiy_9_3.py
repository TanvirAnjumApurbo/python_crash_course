class User:
    def __init__(self, first_name, last_name, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"Their username is {self.username}.")

    def greet_user(self):
        print(f"Hello, {self.username}!")


user_1 = User('John', 'Doe', 30, 'johndoe')
user_2 = User('Jane', 'Smith', 25, 'janesmith')
user_3 = User('Jack', 'Brown', 35, 'jackbrown')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
