current_users = ['admin', 'joe', 'jane', 'john', 'jill']

new_users = ['jill', 'jane', 'jim', 'jake', 'JOE']

# for new_user in new_users:
#     if new_user in current_users:
#         print("Sorry, " + new_user + ", that name is taken.")
#     else:
#         print("Great, " + new_user + ", is available.")

copy_current_users = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in copy_current_users:
        print("Sorry, " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + ", is available.")
