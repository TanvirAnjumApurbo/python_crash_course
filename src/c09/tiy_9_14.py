from random import choice


lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e', ]

winning_combination = [choice(lottery)
                       for _ in range(4)]

print(f"Any ticket matching these four numbers or letters wins the prize: {
      winning_combination}")
