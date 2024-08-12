names = ['John', 'Paul', 'George', 'Ringo']

message0 = f"Hello, How are you {names[0]}?"
message1 = f"Hello, How are you {names[1]}?"
message2 = f"Hello, How are you {names[2]}?"
message3 = f"Hello, How are you {names[3]}?"

print(message0)
print(message1)
print(message2)
print(message3)

for i in names:
    message = f"Hello, How are you {i}?"
    print(message)
