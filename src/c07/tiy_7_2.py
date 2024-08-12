number_of_people = input("How many people are in your dinner group? ")
number_of_people = int(number_of_people)

if number_of_people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
