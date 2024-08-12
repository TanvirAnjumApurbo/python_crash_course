# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt = prompt+"\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello, {name}!")

# age = input("How old are you? ")
# age=int(age) # Convert the input to an integer from a string
# print(age)

# height = input("How tall are you, in inches? ")
# height=int(height)

# if height >= 48:
#   print("\nYou're tall enough to ride!")
# else:
#   print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
