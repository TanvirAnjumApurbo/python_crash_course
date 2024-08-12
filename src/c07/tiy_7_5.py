prompt = "\nTell me your age, and I will tell you the cost of your movie ticket: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 13:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
