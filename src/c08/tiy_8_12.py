def sandwiches(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nYou have requested the following toppings:")
    for topping in toppings:
        print("- " + topping)


sandwiches('ham', 'cheese', 'lettuce')
sandwiches('turkey', 'cheese', 'tomato', 'lettuce')
sandwiches('roast beef', 'cheese', 'onion', 'mayo', 'mustard')
