str1 = 'String 1'
str2 = 'String 2'

print(str1 == str2)

print(str1.lower() == str2.lower())

number1 = 5
number2 = 6

print(number1 == number2)
print(number1 != number2)
print(number1 < number2)
print(number1 > number2)
print(number1 <= number2)
print(number1 >= number2)

age1 = 21
age2 = 22

print(age1 >= 21 and age2 >= 21)
print(age1 >= 21 or age2 >= 21)

mountains = ['fuji', 'everest', 'kilimanjaro', 'denali']
mountain = 'fuji'
if mountain in mountains:
    print(mountain.title() + " is in the list.")

if mountain not in mountains:
    print(mountain.title() + " is not in the list.")
