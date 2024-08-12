guest_list = ["Sara", "Joe", "Mike", "Tom", "Sue"]

print(f"Hello {guest_list[0]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[1]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[2]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[3]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[4]}, I would like to invite you to my dinner party.")

print(f"\n{guest_list[2]} can't make it to the dinner party.")

guest_list.pop(2)
guest_list.insert(2, "Rubab")

print(f"\nHello {guest_list[0]
                 }, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[1]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[2]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[3]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[4]}, I would like to invite you to my dinner party.")

print(f"\nHey {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {
      guest_list[3]}, and {guest_list[4]}, I found a bigger dinner table.")

guest_list.insert(0, "Alia")
guest_list.insert(3, "Laiba")
guest_list.append("Kinza")

print(f"\nHello {guest_list[0]
                 }, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[1]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[2]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[3]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[4]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[5]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[6]}, I would like to invite you to my dinner party.")
print(f"Hello {guest_list[7]}, I would like to invite you to my dinner party.")

print(f"\nHey guys, I can only invite two people for dinner.")
pop_guest_0 = guest_list.pop(0)
print(f"Sorry {pop_guest_0}, I can't invite you to the dinner party.")
pop_guest_1 = guest_list.pop(0)
print(f"Sorry {pop_guest_1}, I can't invite you to the dinner party.")
pop_guest_2 = guest_list.pop(0)
print(f"Sorry {pop_guest_2}, I can't invite you to the dinner party.")
pop_guest_3 = guest_list.pop(0)
print(f"Sorry {pop_guest_3}, I can't invite you to the dinner party.")
pop_guest_4 = guest_list.pop(-2)
print(f"Sorry {pop_guest_4}, I can't invite you to the dinner party.")
pop_guest_5 = guest_list.pop(-2)
print(f"Sorry {pop_guest_5}, I can't invite you to the dinner party.")

print(f"\n{guest_list[0]}, you are still invited to the dinner party.")
print(f"{guest_list[1]}, you are still invited to the dinner party.")

del guest_list[0]
del guest_list[0]
print(guest_list)
