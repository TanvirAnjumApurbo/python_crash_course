from random import choice


lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = [1, 2, 3, 4]

attempts = 0

while True:
    attempts += 1
    winning_combination = [choice(lottery) for _ in range(4)]

    if all(item in winning_combination for item in my_ticket):
        break

print(f"It took {attempts} attempts to match the winning ticket: {my_ticket}")
