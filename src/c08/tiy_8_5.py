def describe_city(city_name, country_name='united states'):
    """Display information about a city."""
    print(city_name.title() + " is in " + country_name.title() + ".")


describe_city('new york')
describe_city('los angeles')
describe_city('dhaka', 'bangladesh')
