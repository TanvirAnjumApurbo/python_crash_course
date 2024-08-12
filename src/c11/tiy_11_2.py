def city_functions(city_name, country_name, population=''):
    """Generate a neatly formatted city and country name."""
    if population:
        return f"{city_name}, {country_name} - population {population}".title()
    else:
        return f"{city_name}, {country_name}".title()
