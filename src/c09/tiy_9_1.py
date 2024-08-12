class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the restaurant name and cuisine type."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is open for business.")


restaurant = Restaurant('The Mean Queen', 'pizza')

print(f"My favorite restaurant is {restaurant.restaurant_name}.")
print(f"They serve {restaurant.cuisine_type} food.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
