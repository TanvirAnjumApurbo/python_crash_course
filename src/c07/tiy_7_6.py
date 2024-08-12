prompt = "\nTell me your age, and I will tell you the cost of your movie ticket: "
prompt += "\n(Enter 'quit' when you are finished.) "

# Active variable to control the loop
active = True

while active:
    age = input(prompt)

    # Conditional test in the while statement to stop the loop
    if age == 'quit':
        active = False  # Setting active to False will stop the loop
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 13:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

        # Optional: Use a break statement to exit the loop (for demonstration)
        if age >= 100:  # Just an arbitrary condition to demonstrate the break statement
            print("You're eligible for a special discount!")
            break  # Exiting the loop if age is 100 or more
