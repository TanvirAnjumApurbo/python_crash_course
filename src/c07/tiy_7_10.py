dream_vacations = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    dream_vacation = input("What is your dream vacation? ")

    dream_vacations[name] = dream_vacation

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, dream_vacation in dream_vacations.items():
    print(f"{name} would like to go to {dream_vacation}.")
