current_users = ['emperor', 'sanguinius', 'leman russ', 'konrad curze', 'fulgrim']
lower_current_users = []
for current_user in current_users:
    lower_current_users.append(current_user.lower())

new_users = ['horus', 'fulgrim', 'lorgar', 'rogal dorn', "lion el'jonson"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"The username: {new_user} has already be taken. Please chose a new username.")
    else:
        print(f"The username: {new_user} is available.")