age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18!')

age = 12
if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is $10.')

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print('Your admission cost is $' + str(price) + '.')

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 20

print('Your admission cost is $' + str(price) + '.')

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print('Your admission cost is $' + str(price) + '.')

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')
