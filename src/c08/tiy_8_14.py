def make_car(manufacturer, model, **car_info):
    """Return a dictionary of information about a car."""
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('toyota', 'prius', color='silver', tow_package=False)
print(car)
