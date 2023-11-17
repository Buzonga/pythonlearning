users = ['admin', 'sanguinius', 'leman russ', 'konrad curze', 'fulgrim']

for user in users:
    if user == 'admin':
        print("Hello admin! Would you like to see a status report?")
    else:
        print(f"Hello {user.title()}! Thank you for logging again.")