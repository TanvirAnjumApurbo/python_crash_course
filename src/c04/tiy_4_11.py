my_pizzas = ['pepperoni', 'sausage', 'mushroom']

friend_pizzas = my_pizzas[:]
my_pizzas.append('cheese')
friend_pizzas.append('veggie')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
