class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the restaurant name and cuisine type."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is open for business.")

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increment the number of customers that have been served."""
        self.number_served += number_served


restaurant = Restaurant('The Mean Queen', 'pizza')

print(f"Number of customers restaurant has served: {restaurant.number_served}")

restaurant.number_served = 10
print(f"Number of customers restaurant has served: {restaurant.number_served}")

restaurant.set_number_served(20)
print(f"Number of customers restaurant has served: {restaurant.number_served}")

restaurant.increment_number_served(30)
print(f"Number of customers restaurant has served: {restaurant.number_served}")
