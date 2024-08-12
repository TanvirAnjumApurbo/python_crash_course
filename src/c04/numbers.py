for value in range(1, 6):
    print(value)

for value in range(6):
    print(value)

even_numbers = list(range(2, 11, 2))  # start at 2, end at 11, increment by 2
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares_2 = [value ** 2 for value in range(1, 11)]
print(squares_2)
