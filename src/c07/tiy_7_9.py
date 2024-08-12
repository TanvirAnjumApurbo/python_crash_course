sandwich_orders = ['pastrami', 'tuna',
                   'pastrami', 'chicken', 'pastrami', 'turkey']
finished_sandwiches = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("I made your "+sandwich+" sandwich.")
    finished_sandwiches.append(sandwich)

print("\nI made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
