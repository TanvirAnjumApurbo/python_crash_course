dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

my_t = (3,)  # This is a tuple with one element; the comma is required.

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
