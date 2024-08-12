buffet = ("chicken", "beef", "mutton", "fish", "vegetables")

print("Original Buffet Menu:")
for item in buffet:
    print(item)

# buffet[0]="crab" # This will cause an error.

buffet = ("crab", "beef", "mutton", "fish", "soup")

print("\nModified Buffet Menu:")
for item in buffet:
    print(item)
