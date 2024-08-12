favorite_places = {
    'joe': ['new york', 'los angeles', 'chicago'],
    'jane': ['paris', 'london', 'rome'],
    'erin': ['tokyo', 'beijing', 'seoul'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
    print("\n")
