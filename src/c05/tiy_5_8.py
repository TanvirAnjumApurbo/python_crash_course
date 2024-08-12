user_names = ['admin', 'john', 'jane', 'joe', 'jill']

for user in user_names:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")
