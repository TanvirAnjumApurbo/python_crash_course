cities = {
    'New York': {
        'Country': 'USA',
        'Population': '8,336,817',
        'Fact': 'The Statue of Liberty was a gift from France.',
    },
    'Los Angeles': {
        'Country': 'USA',
        'Population': '3,979,576',
        'Fact': 'The Hollywood Sign was originally an advertisement for a housing development.',
    },
    'Chicago': {
        'Country': 'USA',
        'Population': '2,693,976',
        'Fact': 'The first Ferris Wheel was built in Chicago.',
    },
}

for city, city_info in cities.items():
    print(f"\n{city}, {city_info['Country']}")
    print(f"Population: {city_info['Population']}")
    print(f"Fact: {city_info['Fact']}")
