number_1 = input("Enter a number: ")
number_2 = input("Enter another number: ")

while True:
    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
    except ValueError:
        print("Sorry, I really needed a number.")
        number_1 = input("Enter a number: ")
        number_2 = input("Enter another number: ")
    else:
        print(f"The sum of {number_1} and {
              number_2} is {number_1 + number_2}.")
        break
