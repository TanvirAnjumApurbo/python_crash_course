prompt = "\nEnter a series of pizza toppings you would like to add to your pizza: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"I will add {topping} to your pizza.")
