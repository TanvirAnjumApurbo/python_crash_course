from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


die_6 = Die()
die_10 = Die(10)
die_20 = Die(20)

for _ in range(10):
    print(f"6-sided die: {die_6.roll_die()}")
    print(f"10-sided die: {die_10.roll_die()}")
    print(f"20-sided die: {die_20.roll_die()}")
    print()
